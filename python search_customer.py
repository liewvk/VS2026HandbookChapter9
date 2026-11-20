import sqlite3
name = input("Name to find: ")
with sqlite3.connect("customers.db") as db:
 rows = db.execute(
"SELECT id, name FROM customers WHERE name = ?",
(name,)).fetchall()
print(rows if rows else "No match")

