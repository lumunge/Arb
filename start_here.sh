#!/bin/bash

# create json files and dirs
mkdir json; cd json; mkdir BLJson LLJson PLJson SAJson;

# create local database
cd ../database; touch bundesliga.db laLiga.db premierLeague.db serieA.db;

cd ../utils; python3 create_dbtables.py

