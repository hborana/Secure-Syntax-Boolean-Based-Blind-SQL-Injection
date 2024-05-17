import sqlite3

def insert_users(user_data):
    # Connect to the SQLite database
    with sqlite3.connect('users.db') as conn:
        # Create a cursor object
        cursor = conn.cursor()
        # Insert multiple records into the users table using executemany()
        cursor.executemany("INSERT INTO users (username, password_hash) VALUES (?, ?)", user_data)
        # Commit the changes to the database
        conn.commit()

# Data to be inserted (as plain text for demonstration; not secure)
users_to_insert = [
    ('Eli', '1234'),
    ('User1', 'abc'),
    ('User2', 'def'),
    ('user3', 'ead'),
    ('user4', 'fce'),
    ('user5', 'cup'),
    ('user6', 'master'),
]

# Insert the user data
insert_users(users_to_insert)
