# Database Management System UI

A Flask-based web application for managing a PostgreSQL database with basic CRUD operations and reporting capabilities.

## Prerequisites

- Python 3.x
- PostgreSQL 14 or higher
- Homebrew (for macOS users)

## Checking Prerequisites

### 1. Check Python Installation
```bash
# Check Python version
python3 --version

# If Python is not installed, install it:
# For macOS
brew install python3
```

### 2. Check PostgreSQL Installation
```bash
# Check if PostgreSQL is installed
postgres --version
# or
psql --version

# Check PostgreSQL service status
brew services list | grep postgresql

# If PostgreSQL is not installed:
brew install postgresql@14

# If PostgreSQL is installed but not running:
brew services start postgresql@14

# Verify PostgreSQL is running correctly:
psql postgres
# If you can connect, type \q to exit
```

### 3. Check Python Dependencies
```bash
# Check if Flask is installed
python3 -c "import flask; print(flask.__version__)"

# Check if psycopg2 is installed
python3 -c "import psycopg2; print(psycopg2.__version__)"

# If either gives an error, install dependencies:
pip3 install flask psycopg2
```

### 4. Validate Database Connection
```bash
# Try connecting to PostgreSQL
psql postgres

# If you see an error like "database dbui does not exist", create it:
createdb dbui

# If you see "connection refused", start PostgreSQL:
brew services start postgresql@14
```

### Common Issues and Solutions:

1. **Python Command Not Found**
   - Use `python3` instead of `python`
   - Ensure Python is in your PATH

2. **PostgreSQL Connection Issues**
   - Check service is running: `brew services list`
   - Verify port 5432 is not in use: `lsof -i :5432`
   - Check PostgreSQL logs: `brew services log postgresql`

3. **Permission Issues**
   - Ensure your user has database creation rights
   - Check PostgreSQL user permissions

## Project Structure

```
DBUI/
├── static/
│   └── db_scripts/
│       ├── Create.txt      # Database schema
│       ├── Inserts.txt     # Sample data
│       └── Views.txt       # Database views
├── templates/
│   ├── base.html          # Base template
│   ├── insert.html        # Insert data form
│   ├── update.html        # Update data form
│   ├── delete.html        # Delete data form
│   ├── query.html         # Query interface
│   └── report.html        # Reports view
└── main.py                # Main application file
```

## Installation

1. **Install PostgreSQL** (if not already installed):
   ```bash
   # For macOS using Homebrew
   brew install postgresql@14
   ```

2. **Start PostgreSQL Service**:
   ```bash
   brew services start postgresql@14
   ```

3. **Install Python Dependencies**:
   ```bash
   pip3 install flask psycopg2
   ```

## Database Setup

1. **Create the Database**:
   ```bash
   createdb dbui
   ```

2. **Create Database Schema**:
   ```bash
   # Navigate to project directory
   cd path/to/DBUI
   
   # Create tables using the schema file
   psql dbui < static/db_scripts/Create.txt
   ```

3. **Verify Database Setup**:
   ```bash
   psql dbui
   # Then type \dt to list all tables
   # Type \q to exit
   ```

## Running the Application

1. **Start the Flask Application**:
   ```bash
   python3 main.py
   ```

2. **Access the Application**:
   - Open your web browser
   - Go to http://127.0.0.1:5000

## Features

### 1. Insert Data
- Navigate to `/insert`
- Enter table name
- Specify columns (comma-separated)
- Provide values (comma-separated)
- Remember to use single quotes for text values

### 2. Query Data
- Navigate to `/query`
- Select table from dropdown
- View all records in the selected table

### 3. Update Data
- Navigate to `/update`
- Specify table name
- Provide SET clause
- Include WHERE clause to target specific records

### 4. Delete Data
- Navigate to `/delete`
- Specify table name
- Include WHERE clause to target specific records

### 5. Reports
- Navigate to `/report`
- View predefined database reports and analytics

## Troubleshooting

1. **Database Connection Issues**:
   - Verify PostgreSQL is running: `brew services list | grep postgresql`
   - Check database exists: `psql -l`
   - Ensure correct database name in `main.py`

2. **Permission Issues**:
   - Check PostgreSQL user permissions
   - Verify database ownership

## Common Operations

### Example Insert:
```sql
Table: Customer
Columns: CustomerID, Name, Email, Password, PhoneNumber
Values: 1, 'John Smith', 'john@email.com', 'password123', '555-0101'
```

### Example Update:
```sql
Table: Customer
Set Clause: Name = 'John A. Smith'
Where Clause: CustomerID = 1
```

## Support

For issues or questions, please:
1. Check the PostgreSQL logs
2. Verify database connection settings
3. Ensure all tables are properly created
4. Check Flask application logs

## Additional Notes

- Remember to backup your database regularly
- Keep PostgreSQL service running while using the application
- Use proper SQL syntax in all operations
- Be careful with DELETE operations as they cannot be undone