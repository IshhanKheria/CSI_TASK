import sys
from database import get_connection, init_db

def query_directories():
    """List all stored directories."""
    with get_connection() as conn:
        results = conn.execute("SELECT path FROM directories").fetchall()
        if results:
            for row in results:
                print(row[0])
        else:
            print("No directories stored.")

if __name__ == "__main__":
    init_db()
    query_directories()
