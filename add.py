import os
import sys
from database import get_connection, init_db
from utils import is_valid_directory

def add_directory(directory):
    """Add a directory to the database."""
    directory = os.path.abspath(directory)

    if not is_valid_directory(directory):
        print("Invalid directory.")
        return

    with get_connection() as conn:
        try:
            conn.execute("INSERT INTO directories (path) VALUES (?)", (directory,))
            print(f"Added: {directory}")
        except:
            print("Directory already exists in the database.")

if __name__ == "__main__":
    init_db()
    if len(sys.argv) != 2:
        print("Usage: python add.py {directory}")
        sys.exit(1)

    add_directory(sys.argv[1])
