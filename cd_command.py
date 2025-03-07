import os
import sys
from utils import is_valid_directory

def change_directory(target_directory):
    """Change directory if valid."""
    target_directory = os.path.abspath(target_directory)

    if not os.path.isdir(target_directory):
        print(f"Error: '{target_directory}' is not a valid directory.", file=sys.stderr)
        return None

    return target_directory  # PowerShell will use this to change directory
