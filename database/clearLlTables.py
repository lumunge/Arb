import conn as dbConn


def truncateLlTables():
    db = "./laLiga.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaLaLiga"""
    btkSql = """DELETE FROM betikaLaLiga"""
    combsSql = """DELETE FROM LLCombinations"""
    cur = conn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(combsSql)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    truncateLlTables()
