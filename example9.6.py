import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE products(id INTEGER PRIMARY KEY, price REAL)')
    db.execute('INSERT INTO products VALUES (?, ?)', (1, 10))
    db.execute('UPDATE products SET price=? WHERE id=?', (12.5, 1))
print(db.execute('SELECT * FROM products').fetchall())

