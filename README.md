# ETL SAT Tax Collection

## Project Purpose and Objectives

The purpose of this project is to create an ETL (Extract, Transform, Load) pipeline for processing and analyzing tax collection data from the SAT (Superintendencia de Administración Tributaria) in Guatemala. The main objectives of the project are:

1. 🗂️ **Data Extraction**: Extract tax collection data from Excel files.
2. 🛠️ **Data Transformation**: Clean and transform the data to match the database schema.
3. 📥 **Data Loading**: Load the transformed data into a SQL Server database.
4. 📊 **Data Analysis**: Provide a web interface for visualizing and analyzing the tax collection data.

## Technologies Used

### Backend

- 🐍 **Python**: The main programming language used for the ETL process and backend development.
- 🌐 **Flask**: A lightweight web framework used to create the web application and API endpoints.
- 🔌 **PyODBC**: A Python library for connecting to the SQL Server database.
- 🐼 **Pandas**: A data manipulation and analysis library used for cleaning and transforming the data.
- 🗄️ **SQLAlchemy**: An ORM (Object-Relational Mapping) library used for database interactions.

### Frontend

- 🖥️ **HTML/CSS**: Used for structuring and styling the web pages.
- ⚙️ **JavaScript**: Used for adding interactivity to the web pages.
- 📈 **Chart.js**: A JavaScript library used for creating interactive charts and visualizations.
- 🎨 **Bootstrap**: A CSS framework used for responsive design and styling.

### Database

- 🗃️ **SQL Server**: The database management system used to store the tax collection data.

## Project Structure

```
.env
.gitignore
app/
    app.py
    db/
        __init__.py
        connection.py
        queries.py
    static/
        dashboard.js
        filters.js
        style.css
        summary.js
    templates/
        base.html
        dashboard.html
        logs.html
        summary.html
        upload.html
    utils/
        __init__.py
        data_cleaning.py
        data_processing.py
data/
    ddl.sql
requirements.txt
uploads/
    .gitkeep
    TR2022.xlsx
    TR2023.xlsx
    TR2024.xlsx
venv/
    Include/
    Lib/
    pyvenv.cfg
    Scripts/
```

## How to Run the Project

1. **Clone the repository**:
    ```sh
    git clone https://github.com/DarwinRuiz/etl-SAT-tax-collection.git
    cd etl-SAT-tax-collection
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Create a SQL Server database using the script in `data/ddl.sql`.
    - Configure the database connection in the `.env` file.

5. **Run the Flask application**:
    ```sh
    python app/app.py
    ```

6. **Access the web application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

## Features

- **File Upload**: Upload Excel files containing tax collection data.
- **Data Cleaning**: Clean and transform the uploaded data to match the database schema.
- **Data Loading**: Load the cleaned data into the SQL Server database.
- **Data Visualization**: Visualize the tax collection data using interactive charts.
- **Logs**: Monitor the data loading process and view logs.

## API Endpoints

- **/api/summary**: Get a summary of the tax collection data.
- **/api/summary/options**: Get unique filter options for activities, departments, and years.
- **/api/logs**: Get logs of the data loading process.


## Author

Darwin Ruiz

---

# ETL SAT Recaudación de Impuestos

## Propósito y Objetivos del Proyecto

El propósito de este proyecto es crear un pipeline ETL (Extract, Transform, Load) para procesar y analizar datos de recaudación de impuestos del SAT (Superintendencia de Administración Tributaria) en Guatemala. Los principales objetivos del proyecto son:

1. 🗂️ **Extracción de Datos**: Extraer datos de recaudación de impuestos de archivos Excel.
2. 🛠️ **Transformación de Datos**: Limpiar y transformar los datos para que coincidan con el esquema de la base de datos.
3. 📥 **Carga de Datos**: Cargar los datos transformados en una base de datos SQL Server.
4. 📊 **Análisis de Datos**: Proporcionar una interfaz web para visualizar y analizar los datos de recaudación de impuestos.

## Tecnologías Utilizadas

### Backend

- 🐍 **Python**: El principal lenguaje de programación utilizado para el proceso ETL y el desarrollo del backend.
- 🌐 **Flask**: Un framework web ligero utilizado para crear la aplicación web y los endpoints de la API.
- 🔌 **PyODBC**: Una biblioteca de Python para conectar con la base de datos SQL Server.
- 🐼 **Pandas**: Una biblioteca de manipulación y análisis de datos utilizada para limpiar y transformar los datos.
- 🗄️ **SQLAlchemy**: Una biblioteca ORM (Mapeo Objeto-Relacional) utilizada para las interacciones con la base de datos.

### Frontend

- 🖥️ **HTML/CSS**: Utilizado para estructurar y estilizar las páginas web.
- ⚙️ **JavaScript**: Utilizado para agregar interactividad a las páginas web.
- 📈 **Chart.js**: Una biblioteca de JavaScript utilizada para crear gráficos y visualizaciones interactivas.
- 🎨 **Bootstrap**: Un framework CSS utilizado para el diseño y estilizado responsivo.

### Base de Datos

- 🗃️ **SQL Server**: El sistema de gestión de bases de datos utilizado para almacenar los datos de recaudación de impuestos.

## Estructura del Proyecto

```
.env
.gitignore
app/
    app.py
    db/
        __init__.py
        connection.py
        queries.py
    static/
        dashboard.js
        filters.js
        style.css
        summary.js
    templates/
        base.html
        dashboard.html
        logs.html
        summary.html
        upload.html
    utils/
        __init__.py
        data_cleaning.py
        data_processing.py
data/
    ddl.sql
requirements.txt
uploads/
    .gitkeep
    TR2022.xlsx
    TR2023.xlsx
    TR2024.xlsx
venv/
    Include/
    Lib/
    pyvenv.cfg
    Scripts/
```

## Cómo Ejecutar el Proyecto

1. **Clonar el repositorio**:
    ```sh
    git clone https://github.com/DarwinRuiz/etl-SAT-tax-collection.git
    cd etl-SAT-tax-collection
    ```

2. **Crear y activar un entorno virtual**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usar `venv\\Scripts\\activate`
    ```

3. **Instalar las dependencias requeridas**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configurar la base de datos**:
    - Crear una base de datos SQL Server utilizando el script en `data/ddl.sql`.
    - Configurar la conexión a la base de datos en el archivo `.env`.

5. **Ejecutar la aplicación Flask**:
    ```sh
    python app/app.py
    ```

6. **Acceder a la aplicación web**:
    Abre tu navegador web y ve a `http://127.0.0.1:5000`.

## Características

- **Carga de Archivos**: Cargar archivos Excel que contienen datos de recaudación de impuestos.
- **Limpieza de Datos**: Limpiar y transformar los datos cargados para que coincidan con el esquema de la base de datos.
- **Carga de Datos**: Cargar los datos limpiados en la base de datos SQL Server.
- **Visualización de Datos**: Visualizar los datos de recaudación de impuestos utilizando gráficos interactivos.
- **Logs**: Monitorear el proceso de carga de datos y ver los logs.

## Endpoints de la API

- **/api/summary**: Obtener un resumen de los datos de recaudación de impuestos.
- **/api/summary/options**: Obtener opciones de filtro únicas para actividades, departamentos y años.
- **/api/logs**: Obtener logs del proceso de carga de datos.

## Autor

Darwin Ruiz