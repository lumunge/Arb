import conn as dbConn


def truncateBlTables():
    db = "./bundesliga.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaBundesliga"""
    btkSql = """DELETE FROM betikaBundesliga"""
    bt22Sql = """DELETE FROM bet22Bundesliga"""
    mlSql = """DELETE FROM melBundesliga"""
    x1Sql = """DELETE FROM x1betBundesliga"""
    combsSql = """DELETE FROM bLCombinations"""
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
    truncateBlTables()
