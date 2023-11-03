import csv
import sqlite3
# Add ten more countries from ten_more_countries.txt to database.db
with open('ten_more_countries.txt', 'r') as f:
    ten_more_countries = csv.reader(f)
    ten_more_countries=list(ten_more_countries)[1:]

conn = sqlite3.connect("database.db")
cur = conn.cursor()
for country in ten_more_countries:
    cur.execute("INSERT INTO countries(id, country, area) VALUES(?,?,?)",(country[0],country[1],country[2]))
conn.commit()
conn.close()