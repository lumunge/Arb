import requests
import json

# Bundesliga URLS
SportPesaSAURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=67358&markets_layout=multiple&o=startTime"
BetikaSAURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=182&sort_id=2&period_id=9&esports=false"
Bet22SAURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetSAUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetSAURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"


def fetchSA(url, jsonFile, site):
    res = requests.get(url)
    print("Fetching serieA odds...")
    print(f"{site} Status: ", res.status_code)
    resJson = json.loads(res.text)
    resObj = json.dumps(resJson, indent=4, sort_keys=True)
    with open(jsonFile, "a") as o:
        o.write(resObj)


if __name__ == "__main__":
    fetchSA(SportPesaSAURL, "../json/SAJson/sportPesaSA.json", "sportpesa")
    fetchSA(BetikaSAURL, "../json/SAJson/betikaSA.json", "betika")
    fetchSA(Bet22SAURL, "../json/SAJson/22betSA.json", "22bet")
    fetchSA(MelBetSAUrl, "../json/SAJson/melbetSA.json", "melbet")
    fetchSA(X1BetSAURL, "../json/SAJson/1xbetSA.json", "1xbet")
