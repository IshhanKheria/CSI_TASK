import os
from utils import is_valid_directory

def change_directory(target_directory):
    if not is_valid_directory(target_directory):
        print(f"Error: '{target_directory}' is not a valid directory.")
        return None

    try:
        os.chdir(target_directory)
        return os.getcwd()  # Return the new directory for PowerShell to use
    except Exception as e:
        print(f"Failed to change directory: {e}")
        return None
