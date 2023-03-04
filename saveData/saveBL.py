import time
import json
import os
import sys

DBPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(DBPATH)

import database


def formatString(str):
    joinedStr = str.replace(" ", "")
    # trimmedStr = joinedStr[0:7]
    return joinedStr.lower()


def formatDate(date):
    return date[5:16]


bLTeams = {  # bundesliga teams
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




# save records to database
def saveSportPesaBL():
    db = "../database/bundesliga.db"
    conn = database.createConnection(db)
    f = open("../json/BLJson/sportPesaBundesLiga.json")
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
    db = "../database/bundesliga.db"
    conn = database.createConnection(db)
    f = open("../json/BLJson/betikaBundesLiga.json")
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



def combineRecords():  # combine table columns
    db = "../database/bundesliga.db"
    conn = database.createConnection(db)
    combineBundesligaSql = f"""INSERT INTO bLCombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, time) 
SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, sp.start_time 
FROM sportpesaBundesliga sp, betikaBundesliga as btk
WHERE sp.home_team=btk.home_team;"""
    cur = conn.cursor()
    cur.execute(combineBundesligaSql)
    conn.commit()
    print("Records combined!")
    return cur.lastrowid


if __name__ == "__main__":  # entry
    saveSportPesaBL()
    saveBetikaBL()
    time.sleep(3)
    combineRecords()
