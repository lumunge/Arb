import conn as dbConn


def truncatePlTables():
    db = "./premierLeague.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaPremierLeague"""
    btkSql = """DELETE FROM betikaPremierLeague"""
    combsSql = """DELETE FROM pLCombinations"""
    cur = conn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(combsSql)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    truncatePlTables()
