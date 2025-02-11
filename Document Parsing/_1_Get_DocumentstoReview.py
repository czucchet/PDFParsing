"""
Configuration file for document sources to be processed
Add document URLs to the list below
"""

DOCUMENT_SOURCES = [
    # "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf",
    "https://www.accenture.com/content/dam/accenture/final/accenture-com/document/Accenture-A-New-Era-of-Generative-AI-for-Everyone.pdf"
    # Add additional document URLs here
    ]

def get_document_sources():
    """Returns the list of document URLs to process"""
    return DOCUMENT_SOURCES