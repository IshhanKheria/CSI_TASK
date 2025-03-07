import sys
from add import add_directory
from remove import remove_directory
from query import query_directories
from jump import jump_to_directory
from database import init_db, update_rank, list_rankings  # Ranking functions

def main():
    if len(sys.argv) < 2:
        print("Usage: clitools {add/remove/query/jump/list-rankings} [directory]")
        return

    command = sys.argv[1].lower()

    # Ensure database is initialized before performing operations
    init_db()

    if command == "add":
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
        best_directory = jump_to_directory(sys.argv[2])
        if best_directory:
            update_rank(best_directory)  # 🔹 Increase ranking when jumped to
            print(best_directory)

    elif command == "list-rankings":  # 🔹 List directory rankings
        list_rankings()

    else:
        print("Invalid command. Usage: clitools {add/remove/query/jump/list-rankings} [directory]")

if __name__ == "__main__":
    main()
