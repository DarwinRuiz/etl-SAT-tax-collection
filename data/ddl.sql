CREATE DATABASE tax_collections;
GO

USE tax_collections;
GO


CREATE SCHEMA collections;
GO


CREATE TABLE collections.Activities (
    activity_id INT NOT NULL IDENTITY,
    activity_code NVARCHAR(50) NOT NULL UNIQUE,
    activity_name NVARCHAR(255) NOT NULL,
    section_name NVARCHAR(255) NULL
);
GO

ALTER TABLE collections.Activities
ADD CONSTRAINT PK_activities PRIMARY KEY (activity_id)
GO



CREATE TABLE collections.Revenues (
    revenue_id INT NOT NULL IDENTITY,             -- Identificador único para cada registro
    year INT NOT NULL,                             -- Año de la recaudación
    month_name NVARCHAR(50) NOT NULL,              -- Nombre del mes en español
    department NVARCHAR(255) NOT NULL,             -- Departamento donde se generó la recaudación
    activity_id INT NOT NULL,                      -- Relación con la tabla Activities
    vat_import DECIMAL(18,2) DEFAULT 0,            -- IVA Importación
    dai DECIMAL(18,2) DEFAULT 0,                   -- Derecho Arancelario a la Importación
    isr DECIMAL(18,2) DEFAULT 0,                   -- Impuesto Sobre la Renta
    iso DECIMAL(18,2) DEFAULT 0,                   -- Impuesto de Solidaridad
    iema DECIMAL(18,2) DEFAULT 0,                  -- Impuesto Específico a la Distribución
    ietaap DECIMAL(18,2) DEFAULT 0,                -- Impuesto Específico a Productos
    iset DECIMAL(18,2) DEFAULT 0,                  -- Impuesto sobre Distribución de Petróleo
    patrimony DECIMAL(18,2) DEFAULT 0,             -- Impuesto al Patrimonio
    vat_domestic DECIMAL(18,2) DEFAULT 0,          -- IVA Doméstico
    beverages DECIMAL(18,2) DEFAULT 0,             -- Recaudación por bebidas
    tobacco DECIMAL(18,2) DEFAULT 0,               -- Recaudación por tabaco
    petroleum DECIMAL(18,2) DEFAULT 0,             -- Recaudación por petróleo
    cement DECIMAL(18,2) DEFAULT 0,                -- Recaudación por cemento
    stamps DECIMAL(18,2) DEFAULT 0,                -- Recaudación por timbres
    vehicles DECIMAL(18,2) DEFAULT 0,              -- Recaudación por vehículos
    iprima DECIMAL(18,2) DEFAULT 0,                -- Impuesto Primario
    others DECIMAL(18,2) DEFAULT 0,                -- Otros impuestos
    total DECIMAL(18,2) DEFAULT 0,                 -- Total recaudado
);

ALTER TABLE collections.Revenues
ADD CONSTRAINT PK_revenues PRIMARY KEY (revenue_id)
GO

ALTER TABLE collections.Revenues
ADD CONSTRAINT FK_revenues_activities FOREIGN KEY (activity_id) REFERENCES collections.Activities(activity_id)
GO

CREATE TABLE collections.Load_logs (
    log_id INT NOT NULL IDENTITY,
    file_name NVARCHAR(255) NOT NULL,      -- Nombre del archivo cargado
    year INT NOT NULL,                     -- Año de la carga
    upload_time DATETIME DEFAULT GETDATE(),-- Fecha y hora de la carga
    total_records INT NOT NULL,            -- Total de registros procesados
    duplicates_detected INT NOT NULL,      -- Duplicados detectados
    status NVARCHAR(50) NOT NULL,          -- Estado: Success o Failed
    error_message NVARCHAR(MAX) NULL       -- Mensaje de error (si aplica)
);
GO

ALTER TABLE collections.Load_logs
ADD CONSTRAINT PK_load_logs PRIMARY KEY (log_id)
GO
