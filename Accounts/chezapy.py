# ChezaCashURL = "https://chezacash.com/api/core-prematch/games?leagueId=17"


#  def createCHPLRecord(conn, record):
#     chsql = """INSERT OR IGNORE INTO chezaPremierLeague(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
#     cur = conn.cursor()
#     cur.execute(chsql, record)
#     conn.commit()
#     return cur.lastrowid

# def saveChPL():
#     db = "./premierLeague.db"
#     conn = createConnection(db)
#     f = open("./jsonFiles/chezaPremierLeague.json")
#     data = json.load(f)
#     with conn:
#         for i in data["games"]:
#             record = (
#                 formatString(i["name"].split("vs.")[0].strip()),
#                 formatString(i["name"].split("vs.")[1].strip()),
#                 i["betTypes"][0]["betLines"][0]["odds"],
#                 i["betTypes"][0]["betLines"][1]["odds"],
#                 i["betTypes"][0]["betLines"][2]["odds"],
#             )
#             createCHPLRecord(conn, record)
#     f.close()
#     print("saved chezapl to db")

# saveChPL()
