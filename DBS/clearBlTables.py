import sqlite3
from sqlite3 import Error

# DB CONNECTION
def createConnection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn


def truncateBlTables():
    db = "./bundesliga.db"
    dbConn = createConnection(db)
    spSql = """DELETE FROM sportpesaBundesliga"""
    btkSql = """DELETE FROM betikaBundesliga"""
    bt22Sql = """DELETE FROM bet22Bundesliga"""
    mlSql = """DELETE FROM melBundesliga"""
    x1Sql = """DELETE FROM x1betBundesliga"""
    combsSql = """DELETE FROM bLCombinations"""
    cur = dbConn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(bt22Sql)
    cur.execute(mlSql)
    cur.execute(combsSql)
    cur.execute(x1Sql)
    dbConn.commit()
    return cur.lastrowid


truncateBlTables()
