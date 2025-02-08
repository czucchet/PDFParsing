import os; import httpx; from dotenv import load_dotenv; import json; import re;import csv
from google import genai;  from google.genai import types
from _1_InputPrompt import get_json_prompt
from _1_SQLServerConnections import get_sql_connection, create_tables, insert_document_data
from _1_Run_Model_Exports import export_reponse_model_dump_json,export_reponse_model_schema

# Load environment variables from .env (make sure GOOGLE_API_KEY is defined there)
load_dotenv(); client = genai.Client()

# Create SQL Server connection
conn = get_sql_connection();  create_tables(conn)

# Ingest the document: download and generate summary using Gemini API
doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
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

insert_document_data(conn, filename,  parsed_json)

conn.close()
