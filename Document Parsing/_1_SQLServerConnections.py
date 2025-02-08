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
    # Basic Document Details
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'document_details')
        BEGIN
            CREATE TABLE document_details (
                filename NVARCHAR(255),
                section NVARCHAR(255),
                field_summary NVARCHAR(200),
                field_description NVARCHAR(200),
                field_value NVARCHAR(MAX),
            )
        END            
    """)
        
    conn.commit()
    cursor.close()

def insert_document_data(conn, filename, parsed_json):
    with conn.cursor() as cursor:
        # Iterate over each top-level section (e.g., basic_document_details, key_content_elements, entities, structured_data)
        for section, fields in parsed_json.items():
            # Ensure that each section is a dict containing field entries
            if isinstance(fields, dict):
                for field, content in fields.items():
                    field_summary = field  # e.g., "title", "Summary", etc.
                    field_description = content.get("field_description", "")
                    value = content.get("value", "")
                    # If value is a list, convert to comma-separated string:
                    field_value = ", ".join(value) if isinstance(value, list) else value
                    cursor.execute("""
                        INSERT INTO document_details (filename, section, field_summary, field_description, field_value)
                        VALUES (?, ?, ?, ?, ?)
                    """, (filename, section, field_summary, field_description, field_value))
        conn.commit()