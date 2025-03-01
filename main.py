import os
import sys
import subprocess

def install_required_packages():
    """Install all packages needed for the application"""
    # Correct package names
    packages = ["httpx", "python-dotenv", "google-generativeai", "pyodbc", "google-api-python-client"]
    
    print("Installing required packages...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--upgrade", "--no-cache-dir", *packages
    ])
    print("Package installation complete.")

def main():
    # 1. Install packages
    install_required_packages()
    
    
    # 2. Run the SQL Server Ingest script
    # If wanting to run the SQL script via main.py uncomment the following lines
    #script_path = os.path.join(os.path.dirname(__file__), "Document Parsing", "_2_SQL Server Ingest_Documents.py")
    
    #if os.path.exists(script_path):
    #    print(f"Running document processing script: {script_path}")
    #    subprocess.check_call([sys.executable, script_path])
    #    print("Document processing complete.")
    #else:
    #    print(f"Error: Could not find {script_path}")
    #    print("Current directory:", os.getcwd())
    #    print("Available files:", os.listdir(os.path.join(os.getcwd(), "Document Parsing")))

if __name__ == "__main__":
    main()