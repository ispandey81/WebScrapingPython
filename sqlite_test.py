import sqlite3
import app
import json
# creates or connects to the db file on your system
conn = sqlite3.connect("test.db")
cur = conn.cursor()
# create public holidays table in sqlite db
cur.execute("""
CREATE TABLE PUBLIC_HOLIDAYS(
    holiday_name text,
    holiday_dates text
)
""")
# invoke the scrape holidays method from app module
dict_to_populate = app.scrape_public_holidays()
# iterate over the returned dictionary and populate the db
for key, value in dict_to_populate.items():
    with conn:
        # json dumps method to store the values as string
        cur.execute("INSERT INTO PUBLIC_HOLIDAYS VALUES(?,?)", (key, json.dumps(value)))

# fetch all rows from the db and print
cur.execute("SELECT * FROM PUBLIC_HOLIDAYS")
for i in cur.fetchall():
    print(i)
conn.close()
