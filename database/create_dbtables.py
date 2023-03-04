import time
import json
import os
import sys

DBPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(DBPATH)

import database




def create_database_tables():
    bldb = "../database/bundesliga.db"
    lldb = "../database/laLiga.db"
    pldb = "../database/premierLeague.db"
    sadb = "../database/serieA.db"
    conn = database.createConnection(bldb)
    conn1 = database.createConnection(lldb)
    conn2 = database.createConnection(pldb)
    conn3 = database.createConnection(sadb)
    # BUNDESLIGA TABLES
    blcombs = """CREATE TABLE bLCombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, time blob)"""

    blbtk = """CREATE TABLE betikaBundesliga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""

    blsp = """CREATE TABLE sportpesaBundesliga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real,
    start_time blob
    )"""


    # LALIGA TABLES
    llcombs = """CREATE TABLE LLCombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, time blob)"""

    llbtk = """CREATE TABLE betikaLaLiga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""

    llsp = """CREATE TABLE sportpesaLaLiga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real,
    start_time blob
    )"""


    # PREMIER LEAGUE TABLES
    plcombs = """CREATE TABLE pLCombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, time blob)"""

    plbtk = """CREATE TABLE betikaPremierLeague(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""

    plsp = """CREATE TABLE sportpesaPremierLeague(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real,
    start_time blob
    )"""


    # SERIES A TABLES
    sasp = """CREATE TABLE sportpesaSA(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real,
    start_time blob
    )"""

    sabtk = """CREATE TABLE betikaSA(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""

    sacombs = """CREATE TABLE SACombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, time blob)"""


    cur = conn.cursor()
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cur3 = conn3.cursor()


    cur.execute(blcombs)
    cur.execute(blbtk)
    cur.execute(blsp)

    cur1.execute(llcombs)
    cur1.execute(llbtk)
    cur1.execute(llsp)

    cur2.execute(plcombs)
    cur2.execute(plbtk)
    cur2.execute(plsp)

    cur3.execute(sacombs)
    cur3.execute(sabtk)
    cur3.execute(sasp)

    conn.commit()
    conn1.commit()
    conn2.commit()
    conn3.commit()
    print("### SUCCESS!! ###")

if __name__ == "__main__":  # entry
    create_database_tables()
