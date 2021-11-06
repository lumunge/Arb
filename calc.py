import itertools
import sqlite3
from sqlite3 import Error


def color(text, r, g, b):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def probability(a, b, c):
    if round((((1 / a) + (1 / b) + (1 / c)) * 100), 2) < 100:
        return color(round((((1 / a) + (1 / b) + (1 / c)) * 100), 2), 127, 255, 0)
    return ""


def genIndices():
    ll = [[2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [4, 7, 10, 13, 16]]
    finalList = list(itertools.product(*ll))
    finale = list()
    for i in finalList:
        if ll[0][0] in i and ll[1][0] in i and ll[2][0] in i:
            continue
        elif ll[0][1] in i and ll[1][1] in i and ll[2][1] in i:
            continue
        elif ll[0][2] in i and ll[1][2] in i and ll[2][2] in i:
            continue
        elif ll[0][3] in i and ll[1][3] in i and ll[2][3] in i:
            continue
        elif ll[0][4] in i and ll[1][4] in i and ll[2][4] in i:
            continue
        elif ll[0][0] in i and ll[1][0] in i:
            continue
        elif ll[0][1] in i and ll[1][1] in i:
            continue
        elif ll[0][2] in i and ll[1][2] in i:
            continue
        elif ll[0][3] in i and ll[1][3] in i:
            continue
        elif ll[0][4] in i and ll[1][4] in i:
            continue
        elif ll[0][0] in i and ll[2][0] in i:
            continue
        elif ll[0][1] in i and ll[2][1] in i:
            continue
        elif ll[0][2] in i and ll[2][2] in i:
            continue
        elif ll[0][3] in i and ll[2][3] in i:
            continue
        elif ll[0][4] in i and ll[2][4] in i:
            continue
        elif ll[1][0] in i and ll[2][0] in i:
            continue
        elif ll[1][1] in i and ll[2][1] in i:
            continue
        elif ll[1][2] in i and ll[2][2] in i:
            continue
        elif ll[1][3] in i and ll[2][3] in i:
            continue
        elif ll[1][4] in i and ll[2][4] in i:
            continue
        else:
            finale.append(i)
    return finale


# DB CONNECTION
def createConnection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn


def getRecords():
    db = "./premierLeague.db"
    conn = createConnection(db)
    getSpSql = """SELECT * FROM pLCombinations"""
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
