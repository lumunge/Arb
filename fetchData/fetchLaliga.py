import requests
import json

# LaLiga URLS
SportPesaLLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=76837&markets_layout=multiple&o=startTime"
BetikaLLURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=14482&sort_id=2&period_id=9&esports=false"



def fetchLaLiga(url, jsonFile, site):
    res = requests.get(url)
    print("Fetching laliga odds...")
    print(f"{site} Status: ", res.status_code)
    resJson = json.loads(res.text)
    resObj = json.dumps(resJson, indent=4, sort_keys=True)
    with open(jsonFile, "a") as o:
        o.write(resObj)


if __name__ == "__main__":
    fetchLaLiga(SportPesaLLURL, "../json/LLJson/sportPesaLaLiga.json", "sportpesa")
    fetchLaLiga(BetikaLLURL, "../json/LLJson/betikaLaLiga.json", "betika")

