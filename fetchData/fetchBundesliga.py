import pip._vendor.requests
import json

# Bundesliga URLS
BetikaBLURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=214&sort_id=2&period_id=9&esports=false"
SportPesaBLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=76390&markets_layout=multiple&o=startTime"



def fetchBundesLiga(url, jsonFile, site):
    res = pip._vendor.requests.get(url)
    print("Fetching bundesliga odds...")
    print(f"{site} Status: ", res.status_code)
    resJson = json.loads(res.text)
    resObj = json.dumps(resJson, indent=4, sort_keys=True)
    with open(jsonFile, "a") as o:
        o.write(resObj)


if __name__ == "__main__":
    fetchBundesLiga(
        SportPesaBLURL, "../json/BLJson/sportPesaBundesLiga.json", "sportpesa"
    )
    fetchBundesLiga(BetikaBLURL, "../json/BLJson/betikaBundesLiga.json", "betika")