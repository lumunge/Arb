import requests
import json

# PREMIER LEAGUE URLS
BetikaPLURL = "https://api.betika.com/v1/uo/matches?&tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=222&sort_id=2&period_id=9&esports=fals"
SportPesaPLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=67600&markets_layout=multiple&o=startTime&pag_count=15&pag_min=1"
Bet22URL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?champs=88637&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"


# FETCH PREMIER LEAGUE DATA FUNCTION
def fetchPremierLeague():
    SPPL = requests.get(SportPesaPLURL)
    BPL = requests.get(BetikaPLURL)
    B22PL = requests.get(Bet22URL)
    MLPL = requests.get(MelBetUrl)
    X1PL = requests.get(X1BetURL)
    print("...fetching premier league data")
    print("sportpesa status: ", SPPL.status_code)
    print("betika status: ", BPL.status_code)
    print("22bet status:", B22PL.status_code)
    print("melbet status:", MLPL.status_code)
    print("1xbet status: ", X1PL.status_code)
    SPPLJson = json.loads(SPPL.text)
    BPLJson = json.loads(BPL.text)
    B22PLJson = json.loads(B22PL.text)
    MLPLJson = json.loads(MLPL.text)
    X1PLJson = json.loads(X1PL.text)
    SPPLObj = json.dumps(SPPLJson, indent=4, sort_keys=True)
    BPLObj = json.dumps(BPLJson, indent=4, sort_keys=True)
    B22PLObj = json.dumps(B22PLJson, indent=4, sort_keys=True)
    MLPLObj = json.dumps(MLPLJson, indent=4, sort_keys=True)
    X1PLObj = json.dumps(X1PLJson, indent=4, sort_keys=True)
    with open("./jsonFiles/sportPesaPremierLeague.json", "a") as o:
        o.write(SPPLObj)
    with open("./jsonFiles/betikaPremierLeague.json", "a") as o:
        o.write(BPLObj)
    with open("./jsonFiles/22betPremierLeague.json", "a") as o:
        o.write(B22PLObj)
    with open("./jsonFiles/melbetPremierLeague.json", "a") as o:
        o.write(MLPLObj)
    with open("./jsonFiles/1xbetPremierLeague.json", "a") as o:
        o.write(X1PLObj)


# FETCH PL DATA CALLS
fetchPremierLeague()
