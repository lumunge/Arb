import requests
import json

# PREMIER LEAGUE URLS
BetikaPLURL = "https://api.betika.com/v1/uo/matches?&tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=222&sort_id=2&period_id=9&esports=fals"
SportPesaPLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=67600&markets_layout=multiple&o=startTime&pag_count=15&pag_min=1"



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
 
