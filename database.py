import os
import sqlite3

DB_PATH = os.path.expanduser("~/.clitools.db")

def init_db():
    """Initialize the SQLite database if not exists."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS directories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE NOT NULL
            )
        """)

def get_connection():
    """Return a database connection."""
    return sqlite3.connect(DB_PATH)
