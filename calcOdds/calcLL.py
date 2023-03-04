import os
import sys

DBPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    os.pardir))
sys.path.append(DBPATH)

import utils
import database

def getRecords():
    db = "../database/laLiga.db"
    conn = database.createConnection(db)
    getSpSql = """SELECT * FROM LLCombinations"""
    cur = conn.cursor()
    cur.execute(getSpSql)
    results = cur.fetchall()
    combinations = utils.genIndices()
    conn.commit()
    sites = {
        2: "sph",
        3: "spx",
        4: "spa",
        5: "btkh",
        6: "btkx",
        7: "btka",
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
                    utils.probability(i[j[0]], i[j[1]], i[j[2]]),
                    i[17],
                )
            )
        print(
            "------------------------------------------------------------------------------------------------------------------"
        )
    return cur.lastrowid


getRecords()
