import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE stock(qty INTEGER CHECK(qty >= 0))')
    db.execute('INSERT INTO stock VALUES (?)', (3,))
    try:
        db.execute('UPDATE stock SET qty = ?', (-1,))
    except sqlite3.IntegrityError:
        print('Invalid stock quantity rejected')
    print(db.execute('SELECT qty FROM stock').fetchone()[0])

