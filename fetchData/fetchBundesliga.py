import requests
import json

# Bundesliga URLS
BetikaBLURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=214&sort_id=2&period_id=9&esports=false"
SportPesaBLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=76390&markets_layout=multiple&o=startTime"
Bet22BLURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetBLUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetBLURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"


def fetchBundesLiga(url, jsonFile, site):
    res = requests.get(url)
    print("...fetching bundesliga data")
    print(f"{site} status: ", res.status_code)
    resJson = json.loads(res.text)
    resObj = json.dumps(resJson, indent=4, sort_keys=True)
    with open(jsonFile, "a") as o:
        o.write(resObj)


fetchBundesLiga(SportPesaBLURL, "../JSON/BLJson/sportPesaBundesLiga.json", "sportpesa")
fetchBundesLiga(BetikaBLURL, "../JSON/BLJson/betikaBundesLiga.json", "betika")
fetchBundesLiga(Bet22BLURL, "../JSON/BLJson/22betBundesLiga.json", "22bet")
fetchBundesLiga(MelBetBLUrl, "../JSON/BLJson/melbetBundesLiga.json", "melbet")
fetchBundesLiga(X1BetBLURL, "../JSON/BLJson/1xbetBundesLiga.json", "1xbet")
