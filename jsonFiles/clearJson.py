import subprocess


jsonFiles = [
    "betikaPremierLeague.json",
    "22betPremierLeague.json",
    "melbetPremierLeague.json",
    "sportPesaPremierLeague.json",
    "1xbetPremierLeague.json",
]


def clearJsonFiles():
    for i in range(len(jsonFiles)):
        returnedVal = subprocess.call(f": > {jsonFiles[i]}", shell=True)
        print(returnedVal)


clearJsonFiles()
