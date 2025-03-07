import os
import sys
from database import get_connection, init_db
from utils import is_valid_directory

def remove_directory(directory):
    """Remove a directory from the database."""
    directory = os.path.abspath(directory)

    if not is_valid_directory(directory):
        print("Invalid directory.")
        return

    with get_connection() as conn:
        result = conn.execute("DELETE FROM directories WHERE path = ?", (directory,))
        if result.rowcount:
            print(f"Removed: {directory}")
        else:
            print("Directory not found.")

if __name__ == "__main__":
    init_db()
    if len(sys.argv) != 2:
        print("Usage: python remove.py {directory}")
        sys.exit(1)

    remove_directory(sys.argv[1])
