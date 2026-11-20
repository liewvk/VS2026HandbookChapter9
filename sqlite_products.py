import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
    db.executemany('INSERT INTO products(name, price) VALUES (?, ?)',
                   [('Keyboard', 69.9), ('Mouse', 25.0), ('Monitor', 499.0)])
    for name, price in db.execute('SELECT name, price FROM products ORDER BY price'):
        print(f'{name}: RM{price:.2f}')

