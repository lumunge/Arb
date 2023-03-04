import conn as dbConn


def truncateSATables():
    db = "./serieA.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaSA"""
    btkSql = """DELETE FROM betikaSA"""
    combsSql = """DELETE FROM SACombinations"""
    cur = conn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(combsSql)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    truncateSATables()
