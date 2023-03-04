import conn as dbConn


def truncateBlTables():
    db = "./bundesliga.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaBundesliga"""
    btkSql = """DELETE FROM betikaBundesliga"""
    combsSql = """DELETE FROM bLCombinations"""
    cur = conn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(combsSql)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    truncateBlTables()
