import time
import json
import sqlite3
from sqlite3 import Error
from fuzzywuzzy import fuzz

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
    trimmedStr = joinedStr[0:7]
    return joinedStr.lower()


# def fuzzyString(str1, str2):
#     return fuzz.ratio(str1.lower(), str2.lower()) > 50


# print(fuzzyString("Bayern", "Bayer 04 Leverkusen"))


def formatDate(date):
    return date[5:16]


bLTeams = {
    "bayern": ["Bayern Munchen", "BAYERN", "Bayern Munich"],
    "dortmund": ["Borussia Dortmund", "DORTMUND"],
    "freiburg": ["SC Freiburg", "FREIBURG", "Freiburg"],
    "vflwolfsburg": ["VfL Wolfsburg", "WOLFSBURG"],
    "leipzig": ["RB Leipzig", "LEIPZIG", "RasenBallsport Leipzig"],
    "leverkusen": ["Bayer Leverkusen", "LEVERKUSEN", "Bayer 04 Leverkusen"],
    "mainz": ["Mainz", "MAINZ", "1. FSV Mainz 05"],
    "unionberlin": ["Union Berlin", "UNION BERLIN"],
    "borussiagladbach": ["Borussia Monchengladbach", "BORUSSIA (MG)"],
    "hoffenheim": ["Hoffenheim", "HOFFENHEIM", "TSG 1899 Hoffenheim"],
    "koln": ["FC Koln", "KOLN", "1. Koln"],
    "bochum": ["VfL Bochum", "Bochum"],
    "herthaberlin": ["Hertha BSC", "HERTHA"],
    "eintrachfrankfurt": ["Eintracht Frankfurt", "EINTRACHT"],
    "stuttgart": ["Stuttgart", "STUTTGART", "VfB Stuttgart"],
    "augsburg": ["Augsburg", "AUGSBURG"],
    "arminiabielefeld": ["Arminia Bielefeld", "BIELEFELD"],
    "greutherfurth": ["Greuther Furth"],
}


def returnKey(str):
    key = [key for key, val in bLTeams.items() if str in val]
    if key:
        return key[0]
    return None


# create records
def createSPBLRecord(conn, record):
    sportpesasql = """INSERT OR IGNORE INTO sportpesaBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd, start_time) VALUES(?, ?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sportpesasql, record)
    conn.commit()
    return cur.lastrowid


def createBBLRecord(conn, record):
    betikasql = """INSERT OR IGNORE INTO betikaBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(betikasql, record)
    conn.commit()
    return cur.lastrowid


def createB22BLRecord(conn, record):
    bet22sql = """INSERT OR IGNORE INTO bet22Bundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(bet22sql, record)
    conn.commit()
    return cur.lastrowid


def createMLBLRecord(conn, record):
    mlsql = """INSERT OR IGNORE INTO melBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(mlsql, record)
    conn.commit()
    return cur.lastrowid


def create1XBBLRecord(conn, record):
    x1sql = """INSERT OR IGNORE INTO x1betBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(x1sql, record)
    conn.commit()
    return cur.lastrowid


# save records
def saveSportPesaBL():
    db = "../DBS/bundesliga.db"
    conn = createConnection(db)
    f = open("../JSON/BLJson/sportPesaBundesLiga.json")
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
            createSPBLRecord(conn, record)
    f.close()
    print("saved sportpesa bundesliga!!")


def saveBetikaBL():
    db = "../DBS/bundesliga.db"
    conn = createConnection(db)
    f = open("../JSON/BLJson/betikaBundesLiga.json")
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
            createBBLRecord(conn, record)
    f.close()
    print("saved betika bundesliga!!")


def saveBet22BL():
    db = "../DBS/bundesliga.db"
    conn = createConnection(db)
    f = open("../JSON/BLJson/22betBundesLiga.json")
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
            createB22BLRecord(conn, record)
    f.close()
    print("saved 22 bet bundesliga!!")


def saveMelBL():
    db = "../DBS/bundesliga.db"
    conn = createConnection(db)
    f = open("../JSON/BLJson/melbetBundesLiga.json")
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
            createMLBLRecord(conn, record)
    f.close()
    print("saved melbet bundesliga!!")


def save1XBL():
    db = "../DBS/bundesliga.db"
    conn = createConnection(db)
    f = open("../JSON/BLJson/1xbetBundesLiga.json")
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
            create1XBBLRecord(conn, record)
    f.close()
    print("saved 1xbet bundesliga!!")


def combineRecords():
    db = "../DBS/bundesliga.db"
    conn = createConnection(db)
    combineBundesligaSql = f"""INSERT INTO bLCombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, bt22h, bt22x, bt22a, mlh, mlx, mla, x1h, x1x, x1a, time) 
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, btt.home_odd, btt.neutral_odd, btt.away_odd, ml.home_odd, ml.neutral_odd, ml.away_odd, x1.home_odd, x1.neutral_odd, x1.away_odd, sp.start_time 
FROM sportpesaBundesliga sp, betikaBundesliga as btk, bet22Bundesliga as btt, melBundesliga as ml, x1betBundesliga as x1
WHERE sp.home_team=btk.home_team
AND sp.home_team=btt.home_team
AND sp.home_team=ml.home_team
AND sp.home_team=x1.home_team"""
    cur = conn.cursor()
    cur.execute(combineBundesligaSql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid


saveSportPesaBL()
saveBetikaBL()
saveBet22BL()
saveMelBL()
save1XBL()
time.sleep(3)
combineRecords()
