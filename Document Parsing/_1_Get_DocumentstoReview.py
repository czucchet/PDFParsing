"""
Configuration file for document sources to be processed
Add document URLs to the list below
"""

import os

DOCUMENT_SOURCES = [
    # "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf",
    # "https://www.accenture.com/content/dam/accenture/final/accenture-com/document/Accenture-A-New-Era-of-Generative-AI-for-Everyone.pdf"
    # Add additional document URLs here
]

# Folder containing documents to process
DOCS_FOLDER = r"C:\Users\Chris\OneDrive\Desktop\Use Case Development\Sample Reports"

def get_document_sources():
    """Returns a list of document sources to process (URLs and file paths)"""
    # Start with remote document sources
    all_sources = list(DOCUMENT_SOURCES)
    
    # Check if documents folder exists
    if os.path.isdir(DOCS_FOLDER):
        # Get all supported documents in the folder (.doc, .docx, .txt)
        local_docs = []
        for filename in os.listdir(DOCS_FOLDER):
            # Support for Word documents and text files
            if filename.lower().endswith(('.doc', '.docx', '.txt', '.pdf')):
                file_path = os.path.join(DOCS_FOLDER, filename)
                local_docs.append(file_path)  # Just use the plain file path
        
        # Add found documents to the sources list
        all_sources.extend(local_docs)
        print(f"Found {len(local_docs)} documents in {DOCS_FOLDER}:")
        for doc in local_docs:
            print(f" - {os.path.basename(doc)}")
    else:
        print(f"Warning: Documents folder not found: {DOCS_FOLDER}")
    
    print(f"Total documents to process: {len(all_sources)}")
    return all_sources