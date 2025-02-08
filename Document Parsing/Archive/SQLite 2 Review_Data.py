import sqlite3

DATABASE_NAME = "document_database.db"

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

cursor.execute("SELECT * FROM documents")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Filename: {row[1]}, Content: {row[2]}")

conn.close()