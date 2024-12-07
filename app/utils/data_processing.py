from db.connection import get_db_connection
from db.queries import merge_activity, insert_revenue, log_load

def process_and_save_data(df, year, file_name):
    """
    Process the cleaned data and save it to the database.
    Logs the operation in the LoadLogs table.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert activities (avoid duplicates using MERGE)
        activities = df[['activity_code', 'activity_name', 'section_name']].drop_duplicates()
        for _, row in activities.iterrows():
            merge_activity(cursor, row['activity_code'], row['activity_name'], row['section_name'])

        conn.commit()

        # Insert revenues
        total_records = len(df)
        duplicates = len(df[df.duplicated()])

        for _, row in df.iterrows():
            # Get activity ID
            cursor.execute('SELECT activity_id FROM collections.Activities WHERE activity_code = ?', row['activity_code'])
            activity_id = cursor.fetchone()[0]

            # Insert revenue data
            insert_revenue(cursor, row, activity_id, year)

        conn.commit()

        # Log success
        log_load(cursor, file_name, year, len(df), duplicates=0, status="Success", error_message=None)
        conn.commit()

    except Exception as e:
        # Log failure in a separate connection
        error_message = str(e)
        conn.rollback()  # Rollback the main connection
        try:
            log_conn = get_db_connection()  # New connection for logging
            log_cursor = log_conn.cursor()
            log_load(log_cursor, file_name, year, total_records=0, duplicates=0, status="Failed", error_message=error_message)
            log_conn.commit()
        except Exception as log_error:
            print(f"Error al registrar log de fallo: {log_error}")
        finally:
            if 'log_conn' in locals():
                log_conn.close()
        raise e

    finally:
        conn.close()
