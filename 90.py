import sqlite3
import csv

conn = sqlite3.connect('database.db')
cur = conn.cursor()

rws = cur.execute("SELECT * FROM countries WHERE area > ?", (2000000,)).fetchall()
with open('customer_data.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['rank', 'country', 'area', 'population'])
    csv_writer.writerows(rws)