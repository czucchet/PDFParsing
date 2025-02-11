# PDF Parsing Project

## Requirements

- Python 3.8 or higher
- An internet connection for downloading required packages

## How to Start

Just run the following command in your terminal (no manual activation or .bat files needed):

```bash
python main.py
```

The script will handle virtual environment creation, package installation, and then execute your program.

## Troubleshooting

- If you see "python not found", ensure Python is installed and in your PATH
- If you get SQL Server errors, verify ODBC Driver 17 is installed
- For permission errors, try running Command Prompt as Administrator

## Configuration

1. Verify your `.env` file contains:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Check SQL Server connection details in `_1_SetSQLServerConnections.py`