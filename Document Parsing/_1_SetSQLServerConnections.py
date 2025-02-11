import pyodbc;import json

# SQL Server connection details
def get_sql_connection():

    SERVER = r"LON001173\SQLEXPRESS02"
    DATABASE = "PDFParse"
    # Use appropriate driver name installed on your machine, e.g., 'ODBC Driver 17 for SQL Server'
    DRIVER = "ODBC Driver 17 for SQL Server"
    conn_str = f"Driver={{{DRIVER}}};Server={SERVER};Database={DATABASE};Trusted_Connection=yes;"
    return pyodbc.connect(conn_str)

# Create a connection and table if it doesn't exist
def create_tables(conn):

    cursor = conn.cursor()
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DocumentAnalysis')
        CREATE TABLE DocumentAnalysis (
            id INT IDENTITY(1,1) PRIMARY KEY,
            filename VARCHAR(255),
            section VARCHAR(100),
            field VARCHAR(500),
            field_description NVARCHAR(MAX),
            value NVARCHAR(MAX)
        )
    """)
        
    conn.commit()
    cursor.close()

def insert_document_data(conn, filename, parsed_json):
    cursor = conn.cursor()
    
    # Iterate through the JSON structure
    for section_name, section_data in parsed_json.items():
        for field_name, field_data in section_data.items():
            # Extract both description and value
            field_description = field_data.get('field description', '')
            field_value = field_data.get('value', '')
            
            # Convert list values to string for storage
            if isinstance(field_value, list):
                field_value = ', '.join(map(str, field_value))
            
            # Insert both description and value
            cursor.execute("""
                INSERT INTO DocumentAnalysis (filename, section, field, field_description, value)
                VALUES (?, ?, ?, ?, ?)
            """, (filename, section_name, field_name, field_description, field_value))
    
    conn.commit()