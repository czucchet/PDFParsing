import os; import httpx; from dotenv import load_dotenv; import json; import re;import csv
from google import genai;  from google.genai import types
from _1_BuildInputPrompt import get_json_prompt
from _1_SetSQLServerConnections import get_sql_connection, create_tables, insert_document_data
from _1_RunModelExports import export_reponse_model_dump_json,export_reponse_model_schema
from _1_Get_DocumentstoReview import get_document_sources

# Load environment variables from .env (make sure GOOGLE_API_KEY is defined there)
load_dotenv(); client = genai.Client()

# Create SQL Server connection
conn = get_sql_connection();  create_tables(conn)

# Process each document from the sources list
for doc_url in get_document_sources():
    
    # Ingest the document: download and generate summary using Gemini API
    filename = doc_url.split("/")[-1]
    doc_data = httpx.get(doc_url).content

    prompt = get_json_prompt()

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            types.Part.from_bytes(data=doc_data, mime_type='application/pdf'), prompt
        ]
    )
    
    cleaned_text = re.sub(r"```json|```", "", response.text).strip()
    parsed_json = json.loads(cleaned_text)

    export_reponse_model_dump_json(response)
    export_reponse_model_schema(response)

    insert_document_data(conn, filename, parsed_json)
    print(f"Completed processing: {filename}")

conn.close()
