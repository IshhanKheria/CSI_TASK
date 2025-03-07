import os
import sqlite3

DB_PATH = os.path.expanduser("~/.clitools.db")

def init_db():
    """Initialize the SQLite database with ranking support."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS directories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE NOT NULL,
                count INTEGER DEFAULT 0
            )
        """)

def get_connection():
    """Return a database connection."""
    return sqlite3.connect(DB_PATH)

def update_rank(directory):
    """Increase the rank (visit count) for a directory."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT count FROM directories WHERE path = ?", (directory,))
        row = cursor.fetchone()
        
        if row:
            new_count = row[0] + 1
            cursor.execute("UPDATE directories SET count = ? WHERE path = ?", (new_count, directory))
        else:
            cursor.execute("INSERT INTO directories (path, count) VALUES (?, ?)", (directory, 1))

        conn.commit()

def get_top_directory(search_term):
    """Return the most visited directory matching the search term."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT path FROM directories 
            WHERE path LIKE ? 
            ORDER BY count DESC LIMIT 1
        """, (f"%{search_term}%",))
        row = cursor.fetchone()
    
    return row[0] if row else None

def list_rankings():
    """List all directories sorted by rank."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT path, count FROM directories ORDER BY count DESC")
        results = cursor.fetchall()
    
    if results:
        print("Rankings:")
        for path, count in results:
            print(f"{path} - {count} visits")
    else:
        print("No directories ranked yet.")
