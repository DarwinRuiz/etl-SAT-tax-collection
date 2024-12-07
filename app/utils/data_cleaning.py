import pandas as pd

def clean_excel_data(filepath):
    """
    Cleans the Excel data:
    - Renames columns to match database schema.
    - Converts month numbers to Spanish month names.
    - Separates activity data for normalization.
    - Converts monetary fields to numeric values.
    """
    # Upload Excel file
    df = pd.read_excel(filepath, header=4, usecols="B:X") 


    # Rename columns to align with the database
    df.rename(columns={
        'Mes': 'month',
        'Código Actividad': 'activity_code',
        'Nombre Actividad': 'activity_name',
        'Nombre Sección': 'section_name',
        'Departamento': 'department',
        'IVA Importación': 'vat_import',
        'DAI': 'dai',
        'ISR': 'isr',
        'ISO': 'iso',
        'IEMA': 'iema',
        'IETAAP': 'ietaap',
        'ISET': 'iset',
        'PATRIMONIO': 'patrimony',
        'IVA Doméstico': 'vat_domestic',
        'BEBIDAS': 'beverages',
        'TABACO': 'tobacco',
        'PETROLEO': 'petroleum',
        'CEMENTO': 'cement',
        'TIMBRES': 'stamps',
        'VEHÍCULOS': 'vehicles',
        'IPRIMA': 'iprima',
        'OTROS': 'others',
        'TOTAL': 'total'
    }, inplace=True)

    # Validate that the required columns exist
    required_columns = [
        'month', 'activity_code', 'activity_name', 'section_name',
        'department', 'vat_import', 'dai', 'isr', 'iso', 'iema',
        'ietaap', 'iset', 'patrimony', 'vat_domestic', 'beverages',
        'tobacco', 'petroleum', 'cement', 'stamps', 'vehicles',
        'iprima', 'others', 'total'
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Convert month numbers to names in Spanish
    meses_esp = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
        9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    df['month_name'] = df['month'].apply(lambda x: meses_esp.get(x, 'Mes Desconocido'))

    # Replace '-' values ​​with NaN
    df.replace('-', None, inplace=True)

    # Convert monetary fields to numbers (fill NaN with 0)
    monetary_columns = [
        'vat_import', 'dai', 'isr', 'iso', 'iema', 'ietaap', 'iset',
        'patrimony', 'vat_domestic', 'beverages', 'tobacco', 'petroleum',
        'cement', 'stamps', 'vehicles', 'iprima', 'others', 'total'
    ]
    for col in monetary_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # drop duplicates
    df.drop_duplicates(inplace=True)

    return df