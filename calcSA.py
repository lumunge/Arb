from utils import genIndices, probability
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


def getRecords():
    db = "./DBS/serieA.db"
    conn = createConnection(db)
    getSpSql = """SELECT * FROM SACombinations"""
    cur = conn.cursor()
    cur.execute(getSpSql)
    results = cur.fetchall()
    combinations = genIndices()
    conn.commit()
    sites = {
        2: "sph",
        3: "spx",
        4: "spa",
        5: "btkh",
        6: "btkx",
        7: "btka",
        8: "bt22h",
        9: "bt22x",
        10: "bt22a",
        11: "mlh",
        12: "mlx",
        13: "mla",
        14: "x1h",
        15: "x1x",
        16: "x1a",
    }
    print(
        "{:<10} {:<10} {:<5} {:<10} {:<5} {:<10} {:<5} {:<10} {:<10} {:<15}".format(
            "Home_Team",
            "Away_Team",
            "site",
            "hOdd",
            "site",
            "nOdd",
            "site",
            "aOdd",
            "ArbProb",
            "Time",
        )
    )
    for i in results:
        for j in combinations:
            print(
                "{:<10} {:<10} {:<5} {:<10} {:<5} {:<10} {:<5} {:<10} {:<10} {:<15}".format(
                    i[0],
                    i[1],
                    sites[j[0]],
                    i[j[0]],
                    sites[j[1]],
                    i[j[1]],
                    sites[j[2]],
                    i[j[2]],
                    probability(i[j[0]], i[j[1]], i[j[2]]),
                    i[17],
                )
            )
        print(
            "------------------------------------------------------------------------------------------------------------------"
        )
    return cur.lastrowid


getRecords()
