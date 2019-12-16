"""Configuration settings for the pyodbc connection string.

This file should be in the same folder as the pyodbc_snippets.ipynb file.

If you're only planning to browse the notebook in read-only mode, you
don't need to modify any of the settings in this file.
"""

# The name of an ODBC driver installed on your local machine.
driver = "ODBC Driver 17 for SQL Server"

# The sample notebook uses the Cloud SQL Proxy running locally.
server = "127.0.0.1"

# The default admin user for a SQL Server instance is named sqlserver.
sql_user = "sqlserver"

# The password specified during creation of the Cloud SQL for SQL Server instance.
sql_password = "ENTER-YOUR-PASSWORD-HERE"
