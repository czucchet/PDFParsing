import os
import httpx
from dotenv import load_dotenv
import json
import re
import csv
from google import genai
from google.genai import types
from _1_BuildInputPrompt import get_json_prompt
from _1_SetSQLServerConnections import get_sql_connection, create_tables, insert_document_data
from _1_RunModelExports import export_reponse_model_dump_json, export_reponse_model_schema
from _1_Get_DocumentstoReview import get_document_sources

# Load environment variables from .env (make sure GOOGLE_API_KEY is defined there)
load_dotenv()
client = genai.Client()

# Create SQL Server connection
conn = get_sql_connection()
create_tables(conn)

# Process each document from the sources list
for doc_source in get_document_sources():
    try:
        print(f"Processing: {doc_source}")
        
        # Get the document filename and determine source type
        if doc_source.startswith(("http://", "https://")):
            # Remote URL
            filename = doc_source.split("/")[-1]
            print(f"Downloading from URL: {doc_source}")
            doc_data = httpx.get(doc_source).content
            mime_type = 'application/pdf'
        else:
            # Local file path
            filename = os.path.basename(doc_source)
            print(f"Reading local file: {doc_source}")
            
            # Read file based on type
            with open(doc_source, "rb") as f:
                doc_data = f.read()
                
            # Determine MIME type based on file extension
            if doc_source.lower().endswith('.pdf'):
                mime_type = 'application/pdf'
            elif doc_source.lower().endswith(('.doc', '.docx')):
                mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            elif doc_source.lower().endswith('.txt'):
                mime_type = 'text/plain'
                # Try multiple encodings
                encodings = ['utf-8', 'latin-1', 'cp1252']
                for encoding in encodings:
                    try:
                        doc_data = doc_data.decode(encoding, errors='replace')
                        break
                    except UnicodeDecodeError:
                        continue
                # Clean the text of problematic characters
                doc_data = ''.join(char for char in doc_data if ord(char) < 65536)
                doc_data = doc_data.encode('utf-8')
            else:
                mime_type = 'application/octet-stream'

        prompt = get_json_prompt()

        # Process document with Gemini API
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[
                types.Part.from_bytes(data=doc_data, mime_type=mime_type), 
                prompt
            ]
        )
        
        cleaned_text = re.sub(r"```json|```", "", response.text).strip()
        parsed_json = json.loads(cleaned_text)

        export_reponse_model_dump_json(response)
        export_reponse_model_schema(response)

        insert_document_data(conn, filename, parsed_json)
        print(f"Completed processing: {filename}")
        
    except Exception as e:
        print(f"Error processing {doc_source}: {str(e)}")
        print("Continuing with next document...")

# Close the database connection
conn.close()
print("All document processing complete!")
