import sqlite3

def execute_query(user_input):
    # Vulnerable to SQL injection
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"  # SQL Injection vulnerability
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

user_input = input("Enter your name: ")
execute_query(user_input)
