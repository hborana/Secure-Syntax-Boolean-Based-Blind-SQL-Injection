import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to retrieve all records from the users table
cursor.execute("SELECT * FROM users")

# Fetch all rows from the query
rows = cursor.fetchall()

# Print the rows
print("ID | Username | Password")
print("------------------------")
for row in rows:
    print(row[0], "|", row[1], "|", row[2])

# Close the connection
conn.close()
