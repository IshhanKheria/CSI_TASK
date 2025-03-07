import os
import sys
from database import get_connection, init_db, update_rank
from rapidfuzz import process

DEFAULT_DIRECTORY = "C:\\Users"  # Default directory if no match is found

def get_all_directories():
    """Retrieve all stored directories, sorted by most visited (highest rank)."""
    with get_connection() as conn:
        results = conn.execute("SELECT path FROM directories ORDER BY count DESC").fetchall()
        return [row[0] for row in results]

def jump_to_directory(keyword):
    """Finds and returns the best matching directory based on the keyword."""
    directories = get_all_directories()
    
    if not directories:
        print("No directories stored.", file=sys.stderr)
        return
    
    keyword_lower = keyword.lower()
    directories_dict = {path.lower(): path for path in directories}

    best_match = process.extractOne(keyword_lower, directories_dict.keys(), score_cutoff=30)

    if best_match:
        best_path = directories_dict[best_match[0]]
        
        # Increase ranking count for this directory
        with get_connection() as conn:
            conn.execute("UPDATE directories SET count = count + 1 WHERE path = ?", (best_path,))

        print(best_path)  # PowerShell will capture this output
    else:
        print(f"No match found for '{keyword}'.", file=sys.stderr)

if __name__ == "__main__":
    init_db()
    if len(sys.argv) != 2:
        print("Usage: python jump.py {directory_keyword}", file=sys.stderr)
        sys.exit(1)

    jump_to_directory(sys.argv[1])
