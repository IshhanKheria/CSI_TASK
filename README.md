
# 🚀 CLI Directory Ranking Tool 📁

---

## 🔍 Overview

The **CLI Directory Ranking Tool** is a Python-based utility inspired by `zoxide`, designed to help you manage and navigate directories efficiently on Windows PowerShell. It uses **SQLite** for persistent storage and **RapidFuzz** for fuzzy search, allowing you to quickly access your most-used directories based on their usage frequency.

---

## ✨ Features

### 1. **Add Directories**
   - Add directories to the database for quick access.
   - Each directory is initialized with a **visit count of 0**.
   - Supports both full and relative paths.

### 2. **Remove Directories**
   - Remove directories from the database with a single command.
   - Ensures only relevant directories are stored.

### 3. **Query Stored Directories**
   - View a complete list of all directories stored in the database.
   - Directories are sorted by their visit count for better organization.

### 4. **Jump to Directory**
   - Search for a directory using a keyword.
   - The system finds the **best match** using fuzzy search and jumps to it.
   - Automatically increases the directory's ranking.

### 5. **List Rankings**
   - Display all directories sorted by their **visit count**.
   - Easily identify the most frequently used directories.

### 6. **Automatic Ranking System**
   - Every time you access a directory, its **visit count is incremented**.
   - Directories are automatically ranked based on usage frequency.

### 7. **Persistent SQLite Database**
   - All directory paths and visit counts are stored in an **SQLite database**.
   - Data is persisted across sessions, ensuring continuity.

---

## ⚙ How It Works

The tool uses Python and SQLite to manage directories effectively. Below is a breakdown of its core components:

### **Utility Functions**

- **`is_valid_directory(path)`**:
   - Verifies if the given path is a valid directory.
   - Ensures only accessible, valid directories are tracked.

---

### **Database Functions**

- **`init_db()`**:
   - Initializes the SQLite database and creates the `directories` table if it doesn't exist.
   - Sets up the schema for tracking directories and their visit counts.

- **`get_connection()`**:
   - Opens and returns a connection to the SQLite database.

- **`update_rank(directory)`**:
   - Increases the visit count for a given directory.
   - If the directory doesn't exist, it is added to the database with a visit count of **1**.

- **`get_top_directory(search_term)`**:
   - Searches for the directory that best matches the provided term and is ranked the highest in terms of visits.
   - Uses **fuzzy search** to handle typos and partial matches.

- **`list_rankings()`**:
   - Lists all directories sorted by their visit counts, starting with the most frequently accessed.
   - Displays directory paths alongside their current visit counts.

- **`get_all_directories()`**:
   - Retrieves all stored directories sorted by rank.

---

### **Core Functions**

- **`change_directory(target_directory)`**:
   - Changes to the specified directory if it is valid.
   - Automatically updates the directory’s rank based on access.

- **`add_directory(directory)`**:
   - Adds a new directory to the database, initializing its rank with 0 visits.
   - Validates the directory path before adding it.

- **`remove_directory(directory)`**:
   - Removes the specified directory from the database.
   - Deletes its entry and associated visit history.

- **`query_directories()`**:
   - Displays all stored directories for easy review.

- **`jump_to_directory(keyword)`**:
   - Finds the best matching directory based on a search keyword.
   - Increases its visit count and ranks it higher in the system.

---

## 🎮 Usage Guide

### **Basic Commands**

#### 1. **Add a Directory**
Add a directory to the database:
```bash
clitools add /path/to/directory
```

#### 2. **Remove a Directory**
Remove a directory from the database:
```bash
clitools remove /path/to/directory
```

#### 3. **Query a Directory**
List all stored directories:
```bash
clitools query
```

#### 4. **Jump a Directory**
Jump to the best-matching directory:
```bash
clitools jump keyword
```

#### 5. **List Rankings**
Display directories sorted by visit count:
```bash
clitools list-rankings
```
---

## 🛠 Installation
### **Prerequisites**
- Python 3.7+
- PowerShell 5.1+
- pip package manager

### **Setup**
#### 1. **Clone the repository:**
```bash
git clone https://github.com/IshhanKheria/CSI_TASK
cd clitools
```
#### 2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
#### 3. **Initialize the SQLite database:**
```bash
python -c "from database import init_db; init_db()"
```
#### 4. **Set up PowerShell profile:**
- Add the following function to your PowerShell profile ($PROFILE):
  - Default profile location: C:\Users\<YourUsername>\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```bash
function clitools {
    param(
        [string]$command,
        [string]$arg
    )

    if ($command -eq "add" -or $command -eq "remove" -or $command -eq "jump") {
        $output = python "C:\path\to\clitools.py" $command $arg
    } elseif ($command -eq "query" -or $command -eq "list-rankings") {
        $output = python "C:\path\to\clitools.py" $command
    } else {
        Write-Host "Usage: clitools {add|query|remove|jump|list-rankings} [directory/keyword]"
        return
    }

    if ($command -eq "jump") {
        if ($output -and (Test-Path -Path $output -PathType Container)) {
            Write-Host "Changed directory to: $output"
            Set-Location -Path $output
        } else {
            Write-Host "No matching directory found. Consider adding the directory first."
        }
    } else {
        $output -split "`n" | ForEach-Object { Write-Host $_ }
    }
}
```
#### 5. **Reload PowerShell:**
```bash
. $PROFILE
```
---

## 📦 Dependencies
- Python 3.7+
- **rapidfuzz** (for fuzzy matching)
- **SQLite3** (built-in with Python)
