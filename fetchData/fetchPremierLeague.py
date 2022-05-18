import requests
import json

# PREMIER LEAGUE URLS
BetikaPLURL = "https://api.betika.com/v1/uo/matches?&tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=222&sort_id=2&period_id=9&esports=fals"
SportPesaPLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=67600&markets_layout=multiple&o=startTime&pag_count=15&pag_min=1"
Bet22PLURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetPLUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?champs=88637&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetPLURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"


def fetchPremierLeague(url, jsonFile, site):
    res = requests.get(url)
    print("Fetching premier league odds...")
    print(f"{site} Status: ", res.status_code)
    resJson = json.loads(res.text)
    resObj = json.dumps(resJson, indent=4, sort_keys=True)
    with open(jsonFile, "a") as o:
        o.write(resObj)


if __name__ == "__main__":
    fetchPremierLeague(
        SportPesaPLURL, "../json/PLJson/sportPesaPremierLeague.json", "sportpesa"
    )
    fetchPremierLeague(BetikaPLURL, "../json/PLJson/betikaPremierLeague.json", "betika")
    fetchPremierLeague(Bet22PLURL, "../json/PLJson/22betPremierLeague.json", "22bet")
    fetchPremierLeague(MelBetPLUrl, "../json/PLJson/melbetPremierLeague.json", "melbet")
    fetchPremierLeague(X1BetPLURL, "../json/PLJson/1xbetPremierLeague.json", "1xbet")
