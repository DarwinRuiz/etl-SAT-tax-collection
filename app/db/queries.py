def merge_activity(cursor, activity_code, activity_name, section_name):


    """
    Inserts an activity into the Activities table, avoiding duplicates using MERGE.
    """
    cursor.execute('''
        MERGE INTO collections.Activities AS target
        USING (SELECT ? AS activity_code, ? AS activity_name, ? AS section_name) AS source
        ON target.activity_code = source.activity_code
        WHEN NOT MATCHED THEN
            INSERT (activity_code, activity_name, section_name)
            VALUES (source.activity_code, source.activity_name, source.section_name);
    ''', (activity_code, activity_name, section_name))


def insert_revenue(cursor, row, activity_id, year):
    """
    Inserts a revenue record into the Revenues table.
    """

    cursor.execute('''
        INSERT INTO collections.Revenues (
            year, month_name, department, activity_id, vat_import, dai, isr, iso,
            iema, ietaap, iset, patrimony, vat_domestic, beverages, tobacco,
            petroleum, cement, stamps, vehicles, iprima, others, total
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''', (
        year, row['month_name'], row['department'], activity_id,
        row['vat_import'], row['dai'], row['isr'], row['iso'],
        row['iema'], row['ietaap'], row['iset'], row['patrimony'],
        row['vat_domestic'], row['beverages'], row['tobacco'],
        row['petroleum'], row['cement'], row['stamps'], row['vehicles'],
        row['iprima'], row['others'], row['total']
    ))

def log_load(cursor, file_name, year, total_records, duplicates, status, error_message=None):
    """
    Inserts a load log into the collections.Load_logs table.
    """
    try:
        cursor.execute('''
            INSERT INTO collections.Load_logs (
                file_name, year, total_records, duplicates_detected, status, error_message
            )
            VALUES (?, ?, ?, ?, ?, ?);
        ''', (file_name, year, total_records, duplicates, status, error_message))
        print(f"Log registrado: {file_name}, {year}, {total_records}, {duplicates}, {status}")
    except Exception as e:
        print(f"Error inserting into logs: {e}")
        raise

