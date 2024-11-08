import sqlite3

def get_all_products():
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
    products = []
    cursor.execute("SELECT * FROM Products")
    prods = cursor.fetchall()
    for product in prods:
        products.append(product)

    connection.commit()
    connection.close()

    return products