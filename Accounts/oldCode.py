# FETCH PREMIER LEAGUE DATA FUNCTION
# def fetchPremierLeague():
#     SPPL = requests.get(SportPesaPLURL)
#     BPL = requests.get(BetikaPLURL)
#     B22PL = requests.get(Bet22URL)
#     MLPL = requests.get(MelBetUrl)
#     X1PL = requests.get(X1BetURL)
#     print("...fetching premier league data")
#     print("sportpesa status: ", SPPL.status_code)
#     print("betika status: ", BPL.status_code)
#     print("22bet status:", B22PL.status_code)
#     print("melbet status:", MLPL.status_code)
#     print("1xbet status: ", X1PL.status_code)
#     SPPLJson = json.loads(SPPL.text)
#     BPLJson = json.loads(BPL.text)
#     B22PLJson = json.loads(B22PL.text)
#     MLPLJson = json.loads(MLPL.text)
#     X1PLJson = json.loads(X1PL.text)
#     SPPLObj = json.dumps(SPPLJson, indent=4, sort_keys=True)
#     BPLObj = json.dumps(BPLJson, indent=4, sort_keys=True)
#     B22PLObj = json.dumps(B22PLJson, indent=4, sort_keys=True)
#     MLPLObj = json.dumps(MLPLJson, indent=4, sort_keys=True)
#     X1PLObj = json.dumps(X1PLJson, indent=4, sort_keys=True)
#     with open("./jsonFiles/sportPesaPremierLeague.json", "a") as o:
#         o.write(SPPLObj)
#     with open("./jsonFiles/betikaPremierLeague.json", "a") as o:
#         o.write(BPLObj)
#     with open("./jsonFiles/22betPremierLeague.json", "a") as o:
#         o.write(B22PLObj)
#     with open("./jsonFiles/melbetPremierLeague.json", "a") as o:
#         o.write(MLPLObj)
#     with open("./jsonFiles/1xbetPremierLeague.json", "a") as o:
#         o.write(X1PLObj)
