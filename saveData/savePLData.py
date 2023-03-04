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



pLTeams = {  # premier league
    "arsenal": ["Arsenal"],
    "astonvilla": ["Aston Villa"],
    "brentford": ["Brentford"],
    "brighton": ["Brighton", "BRIGHTON", "Brighton & Hove Albion"],
    "burnely": ["Burnley", "BURNLEY"],
    "chelsea": ["Chelsea", "CHELSEA"],
    "crystalpalace": ["Crystal Palace"],
    "everton": ["Everton"],
    "leeds": ["Leeds", "Leeds United"],
    "leicester": ["Leicester", "Leicester City"],
    "liverpool": ["Liverpool", "LIVERPOOL"],
    "mancity": ["Manchester City", "MAN CITY"],
    "manunited": ["Manchester Utd", "MAN UTD", "Manchester United"],
    "newcastle": ["Newcastle", "NEWCASTLE", "Newcastle United"],
    "norwichcity": ["Norwich City", "Norwich"],
    "southampton": ["Southampton", "SOUTHAMPTON"],
    "tottenham": ["Tottenham", "TOTTENHAM", "Tottenham Hotspur"],
    "watford": ["Watford", "WATFORD"],
    "westham": ["West Ham", "WEST HAM", "West Ham United"],
    "wolves": ["Wolverhampton", "Wolves", "Wolverhampton Wanderers"],
}


def returnKey(str):
    key = [key for key, val in pLTeams.items() if str in val]
    if key:
        return key[0]
    return None


# save records
def saveSportPesaPL():
    db = "../database/premierLeague.db"
    conn = database.createConnection(db)
    f = open("../json/PLJson/sportPesaPremierLeague.json")
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
            createSPPLRecord(conn, record)
    f.close()
    print("saved sportpesa premier league!!")


def saveBetikaPL():
    db = "../database/premierLeague.db"
    conn = database.createConnection(db)
    f = open("../json/PLJson/betikaPremierLeague.json")
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
            createBPLRecord(conn, record)
    f.close()
    print("saved betika premier league!!")




def combineRecords():
    db = "../database/premierLeague.db"
    conn = database.createConnection(db)
    combinePremierLeagueSql = """INSERT INTO pLCombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, time)
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, sp.start_time
FROM sportpesaPremierLeague sp, betikaPremierLeague as btk
WHERE sp.home_team=btk.home_team;"""
    cur = conn.cursor()
    cur.execute(combinePremierLeagueSql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid


if __name__ == "__main__":
    saveSportPesaPL()
    saveBetikaPL()
    time.sleep(3)
    combineRecords()
