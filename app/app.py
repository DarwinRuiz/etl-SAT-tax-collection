from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from utils.data_cleaning import clean_excel_data
from utils.data_processing import process_and_save_data
from db.connection import get_db_connection
from datetime import datetime
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'your-secret-key'

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if file is present
    if 'file' not in request.files:
        flash('No file selected. Please upload a file.', 'error')
        return redirect(url_for('upload_form'))

    file = request.files['file']
    year = request.form.get('year')

    # Check if the file has a name
    if file.filename == '':
        flash('No file selected. Please upload a valid file.', 'error')
        return redirect(url_for('upload_form'))

    # Check file extension
    if not file.filename.endswith('.xlsx'):
        flash('Invalid file format. Please upload an Excel file (.xlsx).', 'error')
        return redirect(url_for('upload_form'))

    try:
        # Save the file to the uploads folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Clean and process the file
        df = clean_excel_data(filepath)
        process_and_save_data(df, int(year), file.filename)

        # Success Feedback
        flash(f'Successfully uploaded and processed the file for year {year}.', 'success')
        return redirect(url_for('upload_form'))

    except Exception as e:
        # Error feedback
        flash(f'An error occurred while processing the file: {str(e)}', 'error')
        return redirect(url_for('upload_form'))
    


@app.route('/summary', methods=['GET'])
@app.route('/summary/', methods=['GET'])
def summary():
    return render_template('summary.html')


@app.route('/api/summary', methods=['GET'])
def get_summary():
    """
    Devuelve el resumen filtrado según actividad, departamento y año.
    """
    activity = request.args.get('activity')
    department = request.args.get('department')
    year = request.args.get('year')


    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query with optional filters
    query = '''
        SELECT 
            r.year, 
            r.department, 
            a.activity_name, 
            SUM(r.total) AS total_revenue
        FROM collections.Revenues r
        JOIN collections.Activities a ON r.activity_id = a.activity_id
        WHERE 1=1
    '''
    params = []

    if activity:
        query += " AND r.activity_id = ?"
        params.append(activity)
    if department:
        query += " AND r.department = ?"
        params.append(department)
    if year:
        query += " AND r.year = ?"
        params.append(year)

    query += " GROUP BY a.activity_name, r.department, r.year ORDER BY r.year DESC"
    cursor.execute(query, params)
    data = cursor.fetchall()

    # Convert results to JSON
    summary = [{
        'activity_name': row.activity_name,
        'department': row.department,
        'year': row.year,
        'total_revenue': row.total_revenue
    } for row in data]

    conn.close()
    return jsonify(summary)


@app.route('/api/summary/options', methods=['GET'])
def get_filter_options():
    """
    Devuelve las opciones únicas para los filtros de actividad, departamento y año.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Queries to get unique values
        cursor.execute('SELECT activity_id, activity_name FROM collections.Activities ORDER BY activity_name')
        activities = [{'activity_id': row[0], 'activity_name': row[1]} for row in cursor.fetchall()]

        cursor.execute('SELECT DISTINCT department FROM collections.Revenues ORDER BY department')
        departments = [row[0] for row in cursor.fetchall()] 

        cursor.execute('SELECT DISTINCT year FROM collections.Revenues ORDER BY year')
        years = [row[0] for row in cursor.fetchall()]  

        conn.close()

        # Returns data in JSON format
        return jsonify({
            'activities': activities,
            'departments': departments,
            'years': years
        })

    except Exception as e:

        return jsonify({'error': str(e)}), 500


@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Total revenue by department
    cursor.execute('''
        SELECT department, SUM(total) AS total_revenue
        FROM collections.Revenues
        GROUP BY department;
    ''')
    department_revenue = [{'department': row[0], 'total_revenue': float(row[1] or 0)} for row in cursor.fetchall()]

    # Revenue distribution by tax
    cursor.execute('''
        SELECT SUM(vat_import) AS vat_import, SUM(dai) AS dai, SUM(isr) AS isr, SUM(iso) AS iso, SUM(vat_domestic) AS vat_domestic
        FROM collections.Revenues;
    ''')
    tax_distribution = [float(value or 0) for value in cursor.fetchone()]

    # Revenue trends by year
    cursor.execute('''
        SELECT year, SUM(total) AS total_revenue
        FROM collections.Revenues
        GROUP BY year
        ORDER BY year;
    ''')
    yearly_trends = [{'year': row[0], 'total_revenue': float(row[1] or 0)} for row in cursor.fetchall()]

    conn.close()

    return render_template(
        'dashboard.html',
        department_revenue=department_revenue,
        tax_distribution=tax_distribution,
        yearly_trends=yearly_trends
    )


@app.route('/api/logs', methods=['GET'])
def get_logs():
    """
    API para obtener los logs de la tabla Load_logs.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()


        cursor.execute('''
            SELECT log_id, file_name, year, upload_time, total_records, duplicates_detected, status, error_message
            FROM collections.Load_logs
            ORDER BY upload_time DESC;
        ''')
        logs = cursor.fetchall()

        # Convert logs to JSON format
        log_list = [{
            'log_id': log.log_id,
            'file_name': log.file_name,
            'year': log.year,
            'upload_time': log.upload_time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_records': log.total_records,
            'duplicates_detected': log.duplicates_detected,
            'status': log.status,
            'error_message': log.error_message
        } for log in logs]

        conn.close()
        return jsonify(log_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logs', methods=['GET'])
def view_logs():
    """
    Página para visualizar los logs del sistema.
    """
    return render_template('logs.html')


if __name__ == '__main__':
    app.run(debug=True)
