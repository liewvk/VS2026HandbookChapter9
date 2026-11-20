import sqlite3
with sqlite3.connect("customers.db") as db:
 db.execute("CREATE TABLE IF NOT EXISTS customers ("
"id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
db.execute("INSERT OR IGNORE INTO customers(id, name) "
"VALUES (?, ?)", (1, "Amina"))
db.commit()
for row in db.execute("SELECT id, name FROM customers"):
 print(row)

