# Agent Guidelines for ECS_Zambia

## Project Overview

This is a Python data analysis project for Energy Consumption Survey (ECS) data from Zambia. The codebase processes CSV files from field data collection, organizes them by household ID (HHID), and merges timestamp-based measurements.

## Project Structure

```
ECS_Zambia/
├── ECS_Skripte_python/     # Python scripts for data processing
├── ECS_CLEAN/             # Cleaned CSV data files
├── ECS_FUEL/              # Fuel-related data organized by HHID
├── ECS_HHID/             # Data organized by household ID
├── Datenanalyse/         # SQLite database for analysis
└── .vscode/              # VS Code settings
```

## Build & Run Commands

### Running Scripts
```bash
# Run any Python script
python ECS_Skripte_python/<script_name>.py

# Example: Run the HHID sorting script
python ECS_Skripte_python/hh-id-sort.py

# Example: Run timestamp merge
python ECS_Skripte_python/timestamp-merge.py

# Example: Run fuel weight consumption sorting
python ECS_Skripte_python/fuel-weight-consumption-sort.py
```

### Testing
```bash
# Run test script
python ECS_Skripte_python/test.py

# Run specific test function (if pytest is installed)
python -m pytest ECS_Skripte_python/test.py -v
python -m pytest ECS_Skripte_python/test.py::test_function_name -v

# Run single test file with pytest
pytest ECS_Skripte_python/test.py -v
```

### Linting
```bash
# Run flake8 linting
flake8 ECS_Skripte_python/

# Run with specific rules disabled
flake8 ECS_Skripte_python/ --ignore=E501,F401

# Run pylint
pylint ECS_Skripte_python/

# Run ruff (faster alternative)
ruff check ECS_Skripte_python/
```

### Type Checking
```bash
# Run mypy type checking
mypy ECS_Skripte_python/

# Run with strict mode
mypy ECS_Skripte_python/ --strict
```

## Code Style Guidelines

### General
- This is a **Python data analysis project** using pandas and SQLite
- Target Python version: **Python 3.8+**
- Use **4 spaces** for indentation (not tabs)
- Maximum line length: **100 characters** (soft limit, use 88 for black compatibility)
- Always add `encoding='latin-1'` when reading CSV files (field data uses this encoding)

### Imports
- Standard library imports first, then third-party (pandas, numpy), then local
- Group imports by type with blank lines between groups:
  ```python
  import os
  import glob
  import shutil

  import pandas as pd

  import database  # local imports
  ```
- Avoid wildcard imports (`from module import *`)
- Use explicit relative imports for local modules

### Naming Conventions
- **Variables/functions**: `snake_case` (e.g., `ordner_pfad`, `sub_ordner_list`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_ROWS`, `DEFAULT_ENCODING`)
- **Classes**: `PascalCase` (e.g., `DataProcessor`)
- **Modules**: `snake_case` (e.g., `database.py`, `timestamp_merge.py`)
- **Private members**: `_leading_underscore` for internal use

### Type Hints
- **Recommended** for function parameters and return types:
  ```python
  def process_csv(filepath: str, skiprows: int = 0) -> pd.DataFrame:
      ...
  ```
- Use `Optional[X]` instead of `X | None` for Python 3.8 compatibility
- Consider using `typing.IO` for file-like objects

### Error Handling
- Use specific exception types:
  ```python
  try:
      df = pd.read_csv(filepath, encoding='latin-1')
  except FileNotFoundError:
      print(f"File not found: {filepath}")
  except pd.errors.EmptyDataError:
      print(f"Empty file: {filepath}")
      continue
  ```
- Never silently catch all exceptions with bare `except:`
- Log errors appropriately using `print()` or logging module
- Use `continue` or `skip` patterns in loops when handling expected edge cases

### File Operations
- Always specify encoding when reading/writing text files: `encoding='latin-1'`
- Use `os.path.join()` for path construction (cross-platform compatibility)
- Use `exist_ok=True` with `os.makedirs()` to avoid errors on existing directories
- Consider using `pathlib.Path` for modern path handling:
  ```python
  from pathlib import Path
  data_dir = Path("ECS_CLEAN")
  csv_files = list(data_dir.glob("*.csv"))
  ```

### Pandas Conventions
- Use method chaining when possible:
  ```python
  df = (pd.read_csv(filepath, encoding='latin-1')
          .dropna()
          .reset_index(drop=True))
  ```
- Name columns explicitly rather than relying on default headers
- Use `skiprows` parameter to skip metadata rows in CSV files
- Consider using `dtype` parameter for memory efficiency
- Handle `EmptyDataError` when processing multiple files

### Documentation
- Use docstrings for functions and classes:
  ```python
  def merge_timestamp_data(folder_path: str) -> None:
      """
      Merge CSV files by timestamp column.

      Args:
          folder_path: Path to folder containing CSV files

      Returns:
          None: Writes merged file to same directory
      """
  ```
- Add inline comments for non-obvious logic
- Keep comments up-to-date with code changes

### Database Operations
- Use context managers for database connections:
  ```python
  with sqlite3.connect(db_path) as conn:
      df.to_sql("table_name", conn, if_exists="replace")
  ```
- Use parameterized queries to prevent SQL injection:
  ```python
  cursor.execute("SELECT * FROM logs WHERE hhid = ?", (hhid,))
  ```

## Data File Conventions

### CSV File Patterns
- Files follow naming pattern: `{Type}v{Version} {HHID}_{Timestamp}_CLEAN.csv`
- Example: `FUELv2 12854_2025-11-22_09-59-48_CLEAN.csv`
- Skip first row when reading (header row contains metadata)
- Skip 17 rows to reach actual data start in some files
- HHID is located at row index 2, column 1 in metadata section

### Folder Organization
- `ECS_CLEAN/`: Original cleaned CSV files from data collection
- `ECS_FUEL/`: Fuel-related measurements organized by HHID subfolder
- `ECS_HHID/`: General data organized by HHID subfolder

## Testing Guidelines

### Test Structure
- Place tests in `ECS_Skripte_python/test.py` or create `tests/` directory
- Use descriptive test function names: `test_merge_timestamp_data_handles_empty_file()`
- Use pytest fixtures for common setup

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test
python -m pytest ECS_Skripte_python/test.py::test_name

# Run with coverage
python -m pytest --cov=ECS_Skripte_python --cov-report=term-missing
```

## Git Workflow
- Commit message format: `{type}: {description}`
  - Types: `feat`, `fix`, `refactor`, `test`, `docs`
  - Example: `feat: add timestamp merge functionality`
- Create feature branches for new features
- Keep commits focused and atomic

## Security Considerations
- Never commit sensitive data or credentials
- Use environment variables for configuration
- Validate file paths before operations
- Sanitize user input in file operations
