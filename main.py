import urllib.request, urllib.parse, urllib.error
import http
import json
import ssl
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

"""Creating the database."""
print("Initializing Database")
conn = sqlite3.connect('eventdata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Events
    (uid INTEGER NOT NULL PRIMARY KEY UNIQUE,
    etime TEXT, 
    name TEXT, 
    type TEXT,
    summary TEXT,
    lat REAL,
    lon REAL)
    ''')

"""Retrieve data from the API."""

# Set request headers to include user agent
print("Accessing https://polisen.se/api/events")
serviceurl = 'https://polisen.se/api/events'
req = urllib.request.Request(
    serviceurl, 
    data=None,
    headers={
        'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64; 
        rv:109.0) Gecko/20100101 Firefox/109.0'''
    }
)

#Url request
handle = urllib.request.urlopen(req, context=ctx)
data = handle.read().decode()
headers = dict(handle.getheaders())

js = json.loads(data, strict=False)

print('Retrieved', len(data), "characters\n")

count = 0
print("Analysing DB for new data")

conn = sqlite3.connect('eventdata.sqlite')
cur = conn.cursor()

# Update DB with new rows from js

for item in js:
    uid = item["id"]
    
    cur.execute("SELECT uid FROM Events WHERE uid= ?",
        ((uid), ))
    try:
        dbuid = cur.fetchone()[0]
        
        continue
    except:
        count += 1
        pass

    cur.execute('''INSERT INTO Events (uid, etime, name, type, summary, lat, lon)
        VALUES ( ?,?,?,?,?,?,? )''', (item["id"], item["datetime"], item["name"],
        item["type"], item["summary"], item["location"]["gps"].split(',')[1], 
        item["location"]["gps"].split(',')[0] ) )

    conn.commit()
print("Database updated with", count, "records")