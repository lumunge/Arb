import sqlite3
from sqlite3 import Error

# DB CONNECTION
def createConnection(db):
    conn = None
    conn = sqlite3.connect(db)
   # try:
   #     conn = sqlite3.connect(db)
   # except Error as e:
   #     print(e)
    return conn
