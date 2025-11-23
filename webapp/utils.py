# webapp/utils.py (located at C:\Users\Dell\OneDrive\Documents\GitHub\webAppSrsac\webapp\utils.py)

import pandas as pd
import os
from django.conf import settings

def read_excel_table_data(file_name, sheet_name=None):
    """
    Reads data from a specified Excel file and returns it as a list of dictionaries.

    Args:
        file_name (str): The name of the Excel file (e.g., 'table1_agri_rd.xlsx').
                         Assumes the file is in 'your_django_project_root/staticfiles/data/' directory.
        sheet_name (str, optional): The specific sheet name to read. If None, reads the first sheet.

    Returns:
        list of dict: A list of dictionaries, where each dictionary represents a row
                      and keys are column headers. Returns an empty list if file not found
                      or sheet not found.
    """
    # --- CRITICAL FIX HERE ---
    # The 'staticfiles' directory is directly under settings.BASE_DIR (project root),
    # not inside your 'webapp' app directory.
    file_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'data', file_name)
    # -------------------------
    
    # --- DEBUGGING PRINTS (KEEP THESE IN FOR NOW!) ---
    print(f"\n--- DEBUG: Attempting to read Excel file ---")
    print(f"DEBUG: BASE_DIR is: {settings.BASE_DIR}")
    print(f"DEBUG: Constructed file_path: {file_path}")
    print(f"DEBUG: File name requested: {file_name}")
    print(f"DEBUG: Sheet name requested: {sheet_name}")
    # --- END DEBUGGING PRINTS ---

    if not os.path.exists(file_path):
        print(f"ERROR: File NOT FOUND at path: {file_path}")
        # Optional: Try to list directory contents to further debug if needed
        # print(f"DEBUG: Contents of directory {os.path.dirname(file_path)}: {os.listdir(os.path.dirname(file_path))}")
        return []

    try:
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)
            
        data = df.to_dict(orient='records')
        print(f"SUCCESS: Successfully read {len(data)} rows from {file_name}")
        return data
    except Exception as e:
        print(f"ERROR: Failed to read Excel file from {file_path}. Reason: {e}")
        return []