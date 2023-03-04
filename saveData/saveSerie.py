import time
import json
import os
import sys

DBPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(DBPATH)

import database


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
    conn = database.createConnection(db)
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
    conn = database.createConnection(db)
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



def combineRecords():
    db = "../database/serieA.db"
    conn = database.createConnection(db)
    combineSASql = """INSERT INTO SACombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, time) 
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, sp.start_time 
FROM sportpesaSA sp, betikaSA as btk
WHERE sp.home_team=btk.home_team;"""
    cur = conn.cursor()
    cur.execute(combineSASql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid


if __name__ == "__main__":
    saveSportPesaSA()
    saveBetikaSA()
    time.sleep(3)
    combineRecords()
