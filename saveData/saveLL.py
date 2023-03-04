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



llTeams = {  # laliga teams
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
    db = "../database/laLiga.db"
    conn = database.createConnection(db)
    f = open("../json/LLJson/sportPesaLaLiga.json")
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
    db = "../database/laLiga.db"
    conn = database.createConnection(db)
    f = open("../json/LLJson/betikaLaLiga.json")
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




def combineRecords():
    db = "../database/laLiga.db"
    conn = database.createConnection(db)
    combineLaLigaSql = """INSERT INTO LLCombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, time) 
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, sp.start_time 
FROM sportpesaLaLiga sp, betikaLaLiga as btk
WHERE sp.home_team=btk.home_team;"""
    cur = conn.cursor()
    cur.execute(combineLaLigaSql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid

if __name__ == "__main__":
    saveSportPesaLL()
    saveBetikaLL()
    time.sleep(3)
    combineRecords()
