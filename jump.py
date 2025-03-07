import os
import sys
from database import get_connection, init_db
from rapidfuzz import process

DEFAULT_DIRECTORY = "C:\\Users"  # Default directory if no match is found

def get_all_directories():
    """Retrieve all stored directories."""
    with get_connection() as conn:
        results = conn.execute("SELECT path FROM directories").fetchall()
        return [row[0] for row in results]

def jump_to_directory(keyword):
    """Finds and returns the best matching directory based on the keyword."""
    directories = get_all_directories()
    
    if not directories:
        print("No directories stored. Defaulting to:", DEFAULT_DIRECTORY, file=sys.stderr)
        print(DEFAULT_DIRECTORY)
        return
    
    # Convert everything to lowercase for case-insensitive matching
    keyword_lower = keyword.lower()
    directories_lower = {path.lower(): path for path in directories}  # Map lowercase -> original

    # Perform fuzzy matching with a lower cutoff
    best_match = process.extractOne(keyword_lower, directories_lower.keys(), score_cutoff=30)
    
    if best_match:
        print(directories_lower[best_match[0]])  # Print only the path for PowerShell
    else:
        print(f"No match found for '{keyword}'. Defaulting to: {DEFAULT_DIRECTORY}", file=sys.stderr)
        print(DEFAULT_DIRECTORY)  # Print only the path

if __name__ == "__main__":
    init_db()
    if len(sys.argv) != 2:
        print("Usage: python jump.py {directory_keyword}", file=sys.stderr)
        sys.exit(1)

    jump_to_directory(sys.argv[1])
