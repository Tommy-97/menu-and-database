#database_operations.py
import sqlite3

conn = sqlite3.connect('F:\\SQLete\\Forest.sqlite3')


cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')


cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Валера', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Маруся', 25))


cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.commit()


conn.close()
