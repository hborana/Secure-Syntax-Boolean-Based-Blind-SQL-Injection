import sqlite3

# Connect to the database. If the file does not exist, it will be created.
conn = sqlite3.connect('users.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table - USERS
cursor.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
              username TEXT NOT NULL UNIQUE,
              password_hash TEXT NOT NULL)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
