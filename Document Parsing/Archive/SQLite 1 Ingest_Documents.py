from google import genai
from google.genai import types
import httpx
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

client = genai.Client()

# Set up the database (creates table if it doesn't exist)
DATABASE_NAME = "document_database.db"
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        content TEXT
    )
""")
conn.commit()
conn.close()


# Ingest the document: download and generate summary using Gemini API
doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
filename = doc_url.split("/")[-1]
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=[
        types.Part.from_bytes(data=doc_data, mime_type='application/pdf'),
        prompt
    ]
)

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=[
        types.Part.from_bytes(data=doc_data, mime_type='application/pdf'),
        prompt
    ]
)

summary = response.text
print(summary)

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"  # Replace with the actual URL of your PDF

# Store the result in the database
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
cursor.execute("INSERT INTO documents (filename, content) VALUES (?, ?)", (filename, summary))
conn.commit()
conn.close()