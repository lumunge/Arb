import conn as dbConn


def truncateSATables():
    db = "./serieA.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaSA"""
    btkSql = """DELETE FROM betikaSA"""
    bt22Sql = """DELETE FROM bet22SA"""
    mlSql = """DELETE FROM melSA"""
    x1Sql = """DELETE FROM x1betSA"""
    combsSql = """DELETE FROM SACombinations"""
    cur = conn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(bt22Sql)
    cur.execute(mlSql)
    cur.execute(combsSql)
    cur.execute(x1Sql)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    truncateSATables()
