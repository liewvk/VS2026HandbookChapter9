import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, city TEXT)')
    db.execute('INSERT INTO customers VALUES (?, ?, ?)', (1, 'Aina', 'Ipoh'))
    db.execute('UPDATE customers SET city = ? WHERE id = ?', ('Kuala Lumpur', 1))
    result = db.execute('SELECT name, city FROM customers WHERE id = ?', (1,)).fetchone()
    print(result)

