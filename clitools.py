import sys
import os
from cd_command import change_directory
from add import add_directory
from remove import remove_directory
from query import query_directories
from jump import jump_to_directory
from database import init_db

def main():
    if len(sys.argv) < 2:
        print("Usage: clitools {cd/add/remove/query/jump} [directory]")
        return

    command = sys.argv[1].lower()

    # Ensure database is initialized before performing operations
    init_db()

    if command == "cd":
        if len(sys.argv) < 3:
            print("Usage: clitools cd /directoryname/")
            return
        target_directory = sys.argv[2]
        new_directory = change_directory(target_directory)
        if new_directory:
            print(new_directory)  # PowerShell will capture this output

    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: clitools add /directoryname/")
            return
        add_directory(sys.argv[2])

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Usage: clitools remove /directoryname/")
            return
        remove_directory(sys.argv[2])

    elif command == "query":
        query_directories()

    elif command == "jump":
        if len(sys.argv) < 3:
            print("Usage: clitools jump keyword")
            return
        jump_to_directory(sys.argv[2])

    else:
        print("Invalid command. Usage: clitools {cd/add/remove/query/jump} [directory]")

if __name__ == "__main__":
    main()

