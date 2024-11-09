import sqlite3

def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('DELETE FROM Products')
    cursor.execute('INSERT INTO Products (title, description, price) VALUES( ?, ?, ?)',
                   ("Ручка", "ручка как ручка", "25"))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
                   (f"Карандаш", "почти как ручка, только стирать можно", "15"))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
                   ("Линейка", "чтобы отмерять длину какую хочется и рисовать ровные линии", "100"))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
                   ("Ластик", "чтобы стирать карандаш, но если очень постараться ,то и ручку тоже можно ", "50"))

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    products = []
    cursor.execute("SELECT * FROM Products")
    prods = cursor.fetchall()
    for product in prods:
        products.append(product)
    connection.commit()
    connection.close()
    return products

def add_user(username, email, age):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f"{username}", f"{email}", f"{age}", "1000"))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if cursor.fetchone() is None:
        return False
    return True
    connection.commit()
    connection.close()