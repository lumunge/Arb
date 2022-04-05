import conn as dbConn

def truncatePlTables():
    db = "./premierLeague.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaPremierLeague"""
    btkSql = """DELETE FROM betikaPremierLeague"""
    bt22Sql = """DELETE FROM bet22PremierLeague"""
    mlSql = """DELETE FROM melPremierLeague"""
    x1Sql = """DELETE FROM x1betPremierLeague"""
    combsSql = """DELETE FROM pLCombinations"""
    cur = conn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(bt22Sql)
    cur.execute(mlSql)
    cur.execute(combsSql)
    cur.execute(x1Sql)
    conn.commit()
    return cur.lastrowid


truncatePlTables()
