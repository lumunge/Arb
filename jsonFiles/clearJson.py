import subprocess


jsonFiles = [
    "betikaPremierLeague.json",
    "22betPremierLeague.json",
    "melbetPremierLeague.json",
    "sportPesaPremierLeague.json",
    "1xbetPremierLeague.json",
]

for i in range(len(jsonFiles)):
    returnedVal = subprocess.call(f": > {jsonFiles[i]}", shell=True)
    print(returnedVal)


# def test():
#     print("clearing json files...")
