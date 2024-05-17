from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Necessary for session management and flash messages

DATABASE = 'users.db'

@app.route('/')
def index():
    return render_template('login.html')  # Assuming your HTML file is named 'login.html' and is in the templates folder

@app.route('/submit-your-login-form', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Validate the username and password
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Be sure to use parameterized queries to prevent SQL injection
    cursor.execute("SELECT * FROM users WHERE username=? AND password_hash=?", (username, password))
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return 'Login successful!'  # Here you might want to start a session or redirect to a logged-in page
    else:
        return('Invalid credentials, try again!')
        return redirect(url_for('index'))  # Redirect back to the login form

if __name__ == '__main__':
    app.run(debug=True)
