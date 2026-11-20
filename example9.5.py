import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE sales(category TEXT, amount REAL)')
    db.executemany('INSERT INTO sales VALUES (?, ?)', [('Book',30),('Pen',5),('Book',20)])
    for row in db.execute('SELECT category, SUM(amount) FROM sales GROUP BY category'):
        print(row)

