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
    blcombs = """CREATE TABLE bLCombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, bt22h real, bt22x real, bt22a real, mlh real, mlx real, mla real, x1h real, x1x real, x1a real, time blob)"""
    blbt22 = """CREATE TABLE bet22Bundesliga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    blbtk = """CREATE TABLE betikaBundesliga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    blml = """CREATE TABLE melBundesliga(home_team text primary key,
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
    blx1 = """CREATE TABLE x1betBundesliga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""

    # LALIGA TABLES
    llcombs = """CREATE TABLE LLCombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, bt22h real, bt22x real, bt22a real, mlh real, mlx real, mla real, x1h real, x1x real, x1a real, time blob)"""
    llbt22 = """CREATE TABLE bet22LaLiga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    llbtk = """CREATE TABLE betikaLaLiga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    llml = """CREATE TABLE melLaLiga(home_team text primary key,
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
    llx1 = """CREATE TABLE x1betLaLiga(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""

    # PREMIER LEAGUE TABLES
    plcombs = """CREATE TABLE pLCombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, bt22h real, bt22x real, bt22a real, mlh real, mlx real, mla real, x1h real, x1x real, x1a real, time blob)"""
    plbt22 = """CREATE TABLE bet22PremierLeague(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    plbtk = """CREATE TABLE betikaPremierLeague(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    plml = """CREATE TABLE melPremierLeague(home_team text primary key,
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
    plx1 = """CREATE TABLE x1betPremierLeague(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""

    # SERIES A TABLES
    sasp = """CREATE TABLE sportpesaSA(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real,
    start_time blob
    )"""
    sabt22 = """CREATE TABLE bet22SA(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    sabtk = """CREATE TABLE betikaSA(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    saml = """CREATE TABLE melSA(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    sax1 = """CREATE TABLE x1betSA(home_team text primary key,
    away_team text,
    home_odd real,
    neutral_odd real,
    away_odd real)"""
    sacombs = """CREATE TABLE SACombinations(home_team text primary key, away_team text, sph real, spx real, spa real, btkh real, btkx real, btka real, bt22h real, bt22x real, bt22a real, mlh real, mlx real, mla real, x1h real, x1x real, x1a real, time blob)"""


    cur = conn.cursor()
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cur3 = conn3.cursor()


    cur.execute(blcombs)
    cur.execute(blbt22)
    cur.execute(blbtk)
    cur.execute(blml)
    cur.execute(blsp)
    cur.execute(blx1)

    cur1.execute(llcombs)
    cur1.execute(llbt22)
    cur1.execute(llbtk)
    cur1.execute(llml)
    cur1.execute(llsp)
    cur1.execute(llx1)

    cur2.execute(plcombs)
    cur2.execute(plbt22)
    cur2.execute(plbtk)
    cur2.execute(plml)
    cur2.execute(plsp)
    cur2.execute(plx1)

    cur3.execute(sacombs)
    cur3.execute(sabt22)
    cur3.execute(sabtk)
    cur3.execute(saml)
    cur3.execute(sasp)
    cur3.execute(sax1)

    conn.commit()
    conn1.commit()
    conn2.commit()
    conn3.commit()
    print("### Tables Generated Successfully!! ###")

if __name__ == "__main__":  # entry
    create_database_tables()
