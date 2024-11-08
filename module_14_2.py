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
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
cnt_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance_all_users = cursor.fetchone()[0]
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance_all_users = cursor.fetchone()[0]
print(cnt_users)
print(sum_balance_all_users)
print(avg_balance_all_users, sum_balance_all_users/cnt_users)

connection.commit()
connection.close()
