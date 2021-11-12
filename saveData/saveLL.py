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
def createSPLLRecord(conn, record):
    sportpesasql = """INSERT OR IGNORE INTO sportpesaLaLiga(home_team, away_team, home_odd, neutral_odd, away_odd, start_time) VALUES(?, ?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sportpesasql, record)
    conn.commit()
    return cur.lastrowid


def createBLLRecord(conn, record):
    betikasql = """INSERT OR IGNORE INTO betikaLaLiga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(betikasql, record)
    conn.commit()
    return cur.lastrowid


def createB22LLRecord(conn, record):
    bet22sql = """INSERT OR IGNORE INTO bet22LaLiga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(bet22sql, record)
    conn.commit()
    return cur.lastrowid


def createMLLLRecord(conn, record):
    mlsql = """INSERT OR IGNORE INTO melLaLiga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(mlsql, record)
    conn.commit()
    return cur.lastrowid


def create1XBLLRecord(conn, record):
    x1sql = """INSERT OR IGNORE INTO x1betLaLiga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(x1sql, record)
    conn.commit()
    return cur.lastrowid


llTeams = {
    "realsociedad": ["Real Sociedad"],
    "realmadrid": ["Real Madrid"],
    "sevilla": ["Sevilla FC", "SEVILLA", "Sevilla"],
    "atleticomadrid": ["Atletico Madrid"],
    "realbetis": ["Betis", "BETIS", "Real Betis"],
    "rayovallecano": ["Rayo Vallecano", "Vallecano"],
    "osasuna": ["Osasuna"],
    "atleticbilbao": ["Athletic Bilbao", "BILBAO"],
    "barcelona": ["Barcelona", "BARCELONA"],
    "valencia": ["Valencia", "VALENCIA"],
    "espanyol": ["Espanyol", "ESPANYOL"],
    "villarreal": ["Villarreal"],
    "realmallorca": ["Mallorca"],
    "alaves": ["Alaves", "ALAVES", "Deportivo Alaves"],
    "celtavigo": ["Celta Vigo", "CELTA DE VIGO", "Celta"],
    "cadiz": ["Cadiz CF", "Cadiz", "Cádiz"],
    "granada": ["Granada"],
    "elche": ["Elche"],
    "levante": ["Levante", "LEVANTE", "Levante UD"],
    "getafe": ["Getafe", "GETAFE"],
}


def returnKey(str):
    key = [key for key, val in llTeams.items() if str in val]
    if key:
        return key[0]
    return None


# save records
def saveSportPesaLL():
    db = "../DBS/laLiga.db"
    conn = createConnection(db)
    f = open("../JSON/LLJson/sportPesaLaLiga.json")
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
            createSPLLRecord(conn, record)
    f.close()
    print("saved sportpesa la liga!!")


def saveBetikaLL():
    db = "../DBS/laLiga.db"
    conn = createConnection(db)
    f = open("../JSON/LLJson/betikaLaLiga.json")
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
            createBLLRecord(conn, record)
    f.close()
    print("saved betika la liga!!")


def saveBet22LL():
    db = "../DBS/laLiga.db"
    conn = createConnection(db)
    f = open("../JSON/LLJson/22betLaLiga.json")
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
            createB22LLRecord(conn, record)
    f.close()
    print("saved 22 bet la liga!!")


def saveMelLL():
    db = "../DBS/laLiga.db"
    conn = createConnection(db)
    f = open("../JSON/LLJson/melbetLaLiga.json")
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
            createMLLLRecord(conn, record)
    f.close()
    print("saved melbet la liga!!")


def save1XLL():
    db = "../DBS/laLiga.db"
    conn = createConnection(db)
    f = open("../JSON/LLJson/1xbetLaLiga.json")
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
            create1XBLLRecord(conn, record)
    f.close()
    print("saved 1xbet la liga!!")


def combineRecords():
    db = "../DBS/laLiga.db"
    conn = createConnection(db)
    combineLaLigaSql = """INSERT INTO LLCombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, bt22h, bt22x, bt22a, mlh, mlx, mla, x1h, x1x, x1a, time) 
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, btt.home_odd, btt.neutral_odd, btt.away_odd, ml.home_odd, ml.neutral_odd, ml.away_odd, x1.home_odd, x1.neutral_odd, x1.away_odd, sp.start_time 
FROM sportpesaLaLiga sp, betikaLaLiga as btk, bet22LaLiga as btt, melLaLiga as ml, x1betLaLiga as x1
WHERE sp.home_team=btk.home_team
AND sp.home_team=btt.home_team
AND sp.home_team=ml.home_team
AND sp.home_team=x1.home_team;"""
    cur = conn.cursor()
    cur.execute(combineLaLigaSql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid


saveSportPesaLL()
saveBetikaLL()
saveBet22LL()
saveMelLL()
save1XLL()
time.sleep(3)
combineRecords()
