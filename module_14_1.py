import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')
for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)', (f"User{i + 1}", f"example{i + 1}@gmail.com", f"{(i + 1) * 10}", "1000"))

for i in range(0, 10, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, f"{i+1}"))

for i in range(0, 10, 3):
    cursor.execute(f'DELETE FROM Users WHERE id = {i+1}')

connection.commit()
connection.close()