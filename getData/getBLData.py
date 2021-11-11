import json


def probability(a, b, c):
    return round((((1 / a) + (1 / b) + (1 / c)) * 100), 2)


# GET BUNDESLIGA DATA FUNCTIONS
def getSportPesaBLData():
    f = open("../JSON/BLJson/sportPesaBundesLiga.json")
    data = json.load(f)
    print(
        "{:<25} {:<25} {:<10} {:<10} {:<10} {:<25} {:<15}".format(
            "Home_Team", "Away_Team", "hOdd", "nOdd", "aOdd", "Time", "Probability"
        )
    )
    for i in data:
        print(
            "{:<25} {:<25} {:<10} {:<10} {:<10} {:<25} {:<15}".format(
                i["competitors"][0]["name"],
                i["competitors"][1]["name"],
                i["markets"][0]["selections"][0]["odds"],
                i["markets"][0]["selections"][1]["odds"],
                i["markets"][0]["selections"][2]["odds"],
                i["date"],
                probability(
                    float(i["markets"][0]["selections"][0]["odds"]),
                    float(i["markets"][0]["selections"][1]["odds"]),
                    float(i["markets"][0]["selections"][2]["odds"]),
                ),
            )
        )
    f.close()


def getBetikaBLData():
    f = open("../JSON/BLJson/betikaBundesLiga.json")
    data = json.load(f)
    print(
        "{:<25} {:<25} {:<10} {:<10} {:<10} {:<25} {:<15}".format(
            "Home_Team", "Away_Team", "hOdd", "nOdd", "aOdd", "Time", "Probability"
        )
    )
    for i in data["data"]:
        if i["home_odd"] == None or i["neutral_odd"] == None or i["away_odd"] == None:
            continue
        else:
            print(
                "{:<25} {:<25} {:<10} {:<10} {:<10} {:<25} {:<15}".format(
                    (i["home_team"]),
                    (i["away_team"]),
                    i["home_odd"],
                    i["neutral_odd"],
                    i["away_odd"],
                    i["start_time"],
                    probability(
                        float(i["home_odd"]),
                        float(i["neutral_odd"]),
                        float(i["away_odd"]),
                    ),
                )
            )
    f.close()


def get22BetBLData():
    f = open("../JSON/BLJson/22betBundesLiga.json")
    data = json.load(f)
    print(
        "{:<25} {:<25} {:<10} {:<10} {:<10} {:<15}".format(
            "Home_Team", "Away_Team", "hOdd", "nOdd", "aOdd", "Probability"
        )
    )
    for i in data["Value"]:
        if i["E"][0]["C"] == None or i["E"][1]["C"] == None or i["E"][2]["C"] == None:
            continue
        else:
            print(
                "{:<25} {:<25} {:<10} {:<10} {:<10} {:<15}".format(
                    i["O1"],
                    i["O2"],
                    i["E"][0]["C"],
                    i["E"][1]["C"],
                    i["E"][2]["C"],
                    probability(
                        float(i["E"][0]["C"]),
                        float(i["E"][1]["C"]),
                        float(i["E"][2]["C"]),
                    ),
                )
            )

    f.close()


def getMlBLData():
    f = open("../JSON/BLJson/melbetBundesLiga.json")
    data = json.load(f)
    print(
        "{:<25} {:<25} {:<10} {:<10} {:<10}".format(
            "Home_Team", "Away_Team", "hOdd", "nOdd", "aOdd"
        )
    )
    for i in data["Value"]:
        print(
            "{:<25} {:<25} {:<10} {:<10} {:<10}".format(
                i["O1"],
                i["O2"],
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
        )
    f.close()


def getChPlData():
    f = open("./jsonFiles/chezaPremierLeague.json")
    data = json.load(f)
    print(
        "{:<25} {:<25} {:<10} {:<10} {:<10}".format(
            "Home_Team", "Away_Team", "hOdd", "nOdd", "aOdd"
        )
    )
    for i in data["games"]:
        print(
            "{:<25} {:<25} {:<10} {:<10} {:<10}".format(
                i["name"].split("vs.")[0].strip(),
                i["name"].split("vs.")[1].strip(),
                i["betTypes"][0]["betLines"][0]["odds"],
                i["betTypes"][0]["betLines"][1]["odds"],
                i["betTypes"][0]["betLines"][2]["odds"],
            )
        )
    f.close()


def get1XBlData():
    f = open("../JSON/BLJson/1xbetBundesLiga.json")
    data = json.load(f)
    print(
        "{:<25} {:<25} {:<10} {:<10} {:<10}".format(
            "Home_Team", "Away_Team", "hOdd", "nOdd", "aOdd"
        )
    )
    for i in data["Value"]:
        print(
            "{:<25} {:<25} {:<10} {:<10} {:<10}".format(
                i["O1"],
                i["O2"],
                i["E"][0]["C"],
                i["E"][1]["C"],
                i["E"][2]["C"],
            )
        )
    f.close()


getSportPesaBLData()
# getBetikaBLData()
# get22BetBLData()
# getMlBLData()
# get1XBlData()
