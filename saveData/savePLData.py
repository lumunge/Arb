import time
import json
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


def formatString(str):
    joinedStr = str.replace(" ", "")
    trimmedStr = joinedStr[0:5]
    return trimmedStr.lower()


def formatDate(date):
    return date[5:16]


# create records
def createSPPLRecord(conn, record):
    sportpesasql = """INSERT OR IGNORE INTO sportpesaPremierLeague(home_team, away_team, home_odd, neutral_odd, away_odd, start_time) VALUES(?, ?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sportpesasql, record)
    conn.commit()
    return cur.lastrowid


def createBPLRecord(conn, record):
    betikasql = """INSERT OR IGNORE INTO betikaPremierLeague(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(betikasql, record)
    conn.commit()
    return cur.lastrowid


def createB22PLRecord(conn, record):
    bet22sql = """INSERT OR IGNORE INTO bet22PremierLeague(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(bet22sql, record)
    conn.commit()
    return cur.lastrowid


def createMLPLRecord(conn, record):
    mlsql = """INSERT OR IGNORE INTO melPremierLeague(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(mlsql, record)
    conn.commit()
    return cur.lastrowid


def create1XBPLRecord(conn, record):
    x1sql = """INSERT OR IGNORE INTO x1betPremierLeague(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(x1sql, record)
    conn.commit()
    return cur.lastrowid


# save records
def saveSportPesaPL():
    db = "../DBS/premierLeague.db"
    conn = createConnection(db)
    f = open("../JSON/PLJson/sportPesaPremierLeague.json")
    data = json.load(f)
    with conn:
        for i in data:
            record = (
                formatString(i["competitors"][0]["name"]),
                formatString(i["competitors"][1]["name"]),
                i["markets"][0]["selections"][0]["odds"],
                i["markets"][0]["selections"][1]["odds"],
                i["markets"][0]["selections"][2]["odds"],
                formatDate(i["date"]),
            )
            createSPPLRecord(conn, record)
    f.close()
    print("saved sportpesa premier league!!")


def saveBetikaPL():
    db = "../DBS/premierLeague.db"
    conn = createConnection(db)
    f = open("../JSON/PLJson/betikaPremierLeague.json")
    data = json.load(f)
    with conn:
        for i in data["data"]:
            record = (
                formatString(i["home_team"]),
                formatString(i["away_team"]),
                i["home_odd"],
                i["neutral_odd"],
                i["away_odd"],
            )
            createBPLRecord(conn, record)
    f.close()
    print("saved betika premier league!!")


def saveBet22PL():
    db = "../DBS/premierLeague.db"
    conn = createConnection(db)
    f = open("../JSON/PLJson/22betPremierLeague.json")
    data = json.load(f)
    with conn:
        for i in data["Value"]:
            record = (
                formatString(i["O1"]),
                formatString(i["O2"]),
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
            createB22PLRecord(conn, record)
    f.close()
    print("saved 22 bet premier league!!")


def saveMelPL():
    db = "../DBS/premierLeague.db"
    conn = createConnection(db)
    f = open("../JSON/PLJson/melbetPremierLeague.json")
    data = json.load(f)
    with conn:
        for i in data["Value"]:
            record = (
                formatString(i["O1"]),
                formatString(i["O2"]),
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
            createMLPLRecord(conn, record)
    f.close()
    print("saved melbet to db")


def save1XPL():
    db = "../DBS/premierLeague.db"
    conn = createConnection(db)
    f = open("../JSON/PLJson/1xbetPremierLeague.json")
    data = json.load(f)
    with conn:
        for i in data["Value"]:
            record = (
                formatString(i["O1"]),
                formatString(i["O2"]),
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
            create1XBPLRecord(conn, record)
    f.close()
    print("saved 1xbet to db")


def combineRecords():
    db = "../DBS/premierLeague.db"
    conn = createConnection(db)
    combinePremierLeagueSql = """INSERT INTO pLCombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, bt22h, bt22x, bt22a, mlh, mlx, mla, x1h, x1x, x1a, time) 
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, btt.home_odd, btt.neutral_odd, btt.away_odd, ml.home_odd, ml.neutral_odd, ml.away_odd, x1.home_odd, x1.neutral_odd, x1.away_odd, sp.start_time 
FROM sportpesaPremierLeague sp, betikaPremierLeague as btk, bet22PremierLeague as btt, melPremierLeague as ml, x1betPremierLeague as x1
WHERE sp.home_team=btk.home_team
AND sp.home_team=btt.home_team
AND sp.home_team=ml.home_team
AND sp.home_team=x1.home_team;"""
    cur = conn.cursor()
    cur.execute(combinePremierLeagueSql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid


saveSportPesaPL()
saveBetikaPL()
saveBet22PL()
saveMelPL()
save1XPL()
time.sleep(3)
combineRecords()
