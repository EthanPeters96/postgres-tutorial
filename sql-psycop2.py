# Import the PostgreSQL adapter for Python
import psycopg2

# Create a connection to the 'chinook' database
connection = psycopg2.connect(database="chinook")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Fetch all rows from the executed query
results = cursor.fetchall()

# Fetch a single row from the executed query
# result = cursor.fetchone()

# Close the database connection
connection.close()

# Print each row from the results
for result in results:
    print(result)

