import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

rws = cur.execute("SELECT country FROM countries WHERE area > ?", (2000000,)).fetchall()
for row in rws:
    print(row[0])
