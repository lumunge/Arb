import requests
import json

# Bundesliga URLS
SportPesaLLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=76837&markets_layout=multiple&o=startTime"
BetikaLLURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=14482&sort_id=2&period_id=9&esports=false"
Bet22LLURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetLLUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetLLURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"


def fetchLaLiga(url, jsonFile, site):
    res = requests.get(url)
    print("Fetching laliga odds...")
    print(f"{site} Status: ", res.status_code)
    resJson = json.loads(res.text)
    resObj = json.dumps(resJson, indent=4, sort_keys=True)
    with open(jsonFile, "a") as o:
        o.write(resObj)


fetchLaLiga(SportPesaLLURL, "../json/LLJson/sportPesaLaLiga.json", "sportpesa")
fetchLaLiga(BetikaLLURL, "../json/LLJson/betikaLaLiga.json", "betika")
fetchLaLiga(Bet22LLURL, "../json/LLJson/22betLaLiga.json", "22bet")
fetchLaLiga(MelBetLLUrl, "../json/LLJson/melbetLaLiga.json", "melbet")
fetchLaLiga(X1BetLLURL, "../json/LLJson/1xbetLaLiga.json", "1xbet")
