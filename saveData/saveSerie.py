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
def createSPSARecord(conn, record):
    sportpesasql = """INSERT OR IGNORE INTO sportpesaSA(home_team, away_team, home_odd, neutral_odd, away_odd, start_time) VALUES(?, ?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sportpesasql, record)
    conn.commit()
    return cur.lastrowid


def createBSARecord(conn, record):
    betikasql = """INSERT OR IGNORE INTO betikaSA(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(betikasql, record)
    conn.commit()
    return cur.lastrowid


def createB22SARecord(conn, record):
    bet22sql = """INSERT OR IGNORE INTO bet22SA(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(bet22sql, record)
    conn.commit()
    return cur.lastrowid


def createMLSARecord(conn, record):
    mlsql = """INSERT OR IGNORE INTO melSA(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(mlsql, record)
    conn.commit()
    return cur.lastrowid


def create1XBSARecord(conn, record):
    x1sql = """INSERT OR IGNORE INTO x1betSA(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(x1sql, record)
    conn.commit()
    return cur.lastrowid


saTeams = {
    "napoli": ["Napoli", "NAPOLI"],
    "acmilan": ["AC Milan", "Milan"],
    "intermilan": ["Inter", "Internazionale Milano"],
    "atalanta": ["Atalanta", "ATALANTA"],
    "lazio": ["Lazio", "LAZIO"],
    "roma": ["Roma", "ROMA"],
    "fiorentina": ["Fiorentina", "FIORENTINA"],
    "juventus": ["Juventus", "JUVENTUS"],
    "bologna": ["Bologna", "BOLOGNA", "Bologna 1909"],
    "verona": ["Verona", "HELLAS VERONA", "Hellas Verona"],
    "empoli": ["Empoli"],
    "torino": ["Torino", "TORINO"],
    "sassuolo": ["Sassuolo", "SASSUOLO", "Sassuolo Calcio"],
    "udinese": ["Udinese", "UDINESE", "Udinese Calcio"],
    "venezia": ["Venezia", "Venezia", "Unione Venezia"],
    "spezia": ["Spezia", "Spezia Calcio"],
    "genoa": ["Genoa", "GENOA"],
    "sampdoria": ["Sampdoria", "SAMPDORIA"],
    "salernitana": ["Salernitana", "Salernitana 1919"],
    "cagliari": ["Cagliari", "CAGLIARI", "Cagliari Calcio"],
}


def returnKey(str):
    key = [key for key, val in saTeams.items() if str in val]
    if key:
        return key[0]
    return None


# save records
def saveSportPesaSA():
    db = "../database/serieA.db"
    conn = createConnection(db)
    f = open("../json/SAJson/sportPesaSA.json")
    data = json.load(f)
    with conn:
        for i in data:
            record = (
                returnKey(i["competitors"][0]["name"]),
                returnKey(i["competitors"][1]["name"]),
                i["markets"][0]["selections"][0]["odds"],
                i["markets"][0]["selections"][1]["odds"],
                i["markets"][0]["selections"][2]["odds"],
                formatDate(i["date"]),
            )
            createSPSARecord(conn, record)
    f.close()
    print("saved sportpesa serie a!!")


def saveBetikaSA():
    db = "../database/serieA.db"
    conn = createConnection(db)
    f = open("../json//SAJson/betikaSA.json")
    data = json.load(f)
    with conn:
        for i in data["data"]:
            record = (
                returnKey(i["home_team"]),
                returnKey(i["away_team"]),
                i["home_odd"],
                i["neutral_odd"],
                i["away_odd"],
            )
            createBSARecord(conn, record)
    f.close()
    print("saved betika serie a!!")


def saveBet22SA():
    db = "../database/serieA.db"
    conn = createConnection(db)
    f = open("../json/SAJson/22betSA.json")
    data = json.load(f)
    with conn:
        for i in data["Value"]:
            record = (
                returnKey(i["O1"]),
                returnKey(i["O2"]),
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
            createB22SARecord(conn, record)
    f.close()
    print("saved 22 bet serie a!!")


def saveMelSA():
    db = "../database/serieA.db"
    conn = createConnection(db)
    f = open("../json/SAJson/melbetSA.json")
    data = json.load(f)
    with conn:
        for i in data["Value"]:
            record = (
                returnKey(i["O1"]),
                returnKey(i["O2"]),
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
            createMLSARecord(conn, record)
    f.close()
    print("saved melbet serie a!!")


def save1XSA():
    db = "../database/serieA.db"
    conn = createConnection(db)
    f = open("../json/SAJson/1xbetSA.json")
    data = json.load(f)
    with conn:
        for i in data["Value"]:
            record = (
                returnKey(i["O1"]),
                returnKey(i["O2"]),
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
            create1XBSARecord(conn, record)
    f.close()
    print("saved 1xbet serie a!!")


def combineRecords():
    db = "../database/serieA.db"
    conn = createConnection(db)
    combineSASql = """INSERT INTO SACombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, bt22h, bt22x, bt22a, mlh, mlx, mla, x1h, x1x, x1a, time) 
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, btt.home_odd, btt.neutral_odd, btt.away_odd, ml.home_odd, ml.neutral_odd, ml.away_odd, x1.home_odd, x1.neutral_odd, x1.away_odd, sp.start_time 
FROM sportpesaSA sp, betikaSA as btk, bet22SA as btt, melSA as ml, x1betSA as x1
WHERE sp.home_team=btk.home_team
AND sp.home_team=btt.home_team
AND sp.home_team=ml.home_team
AND sp.home_team=x1.home_team;"""
    cur = conn.cursor()
    cur.execute(combineSASql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid


saveSportPesaSA()
saveBetikaSA()
saveBet22SA()
saveMelSA()
save1XSA()
time.sleep(3)
combineRecords()
