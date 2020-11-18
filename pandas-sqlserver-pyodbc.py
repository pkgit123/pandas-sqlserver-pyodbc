# Step 1: Install pyodbc
import pyodbc
import pandas as pd

# Step 2: retrieve server name (from SQL Server client login)
str_server_name = 'SERVER_NAME'

# Step 3: obtain database name (from SQL Server client -> databases)
str_db_name = 'DATABASE_NAME'

# =================================================
# print out list of available tables
# =================================================

# create connection between Python (pyodbc) and SQL Server
str_trusted_connection = f'Server={str_server_name};Database={str_db_name};Trusted_Connection=yes;'
conn = pyodbc.connect('Driver={SQL Server};'+str_trusted_connection)

# print out list of available tables from pyodbc connection
cursor = conn.cursor()
count_tables = 0
limit_tables = 40
for row in cursor.tables():
    if count_tables < limit_tables:
        print(count_tables, '\t', row.table_name)
        count_tables+=1
        
# =================================================
# Query table and load into dataframe
# =================================================

# Step 4: Get the table name using schema and table
# concept of database -> schema -> table
str_table_name = '[SCHEMA_NAME].[TABLE_NAME]'

# Step 5: create connection between Python (pyodbc) and SQL Server
str_trusted_connection = f'Server={str_server_name};Database={str_db_name};Trusted_Connection=yes;'
conn = pyodbc.connect('Driver={SQL Server};'+str_trusted_connection)

# Step 6: create sql query string (only top 1K records)
str_sql_query = f'''
    SELECT TOP (1000) * 
    FROM {str_table_name};
'''

# Step 7: create pandas dataframe using query string and pyodbc connection
df_test = pd.read_sql_query(str_sql_query, conn)

# preview table
print( df_test.shape) )
print( df_test.head() ) 

