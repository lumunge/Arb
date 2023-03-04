#!/bin/bash

echo "clearing json files..."
cd json/PLJson/ && rm -rf *
echo "success!"
sleep 2

echo "clearing tables..."
cd ../../database/ && python3 clearPlTables.py
echo "success!"
sleep 2

echo "fetching data..."
cd ../fetchData/ && python3 fetchPremierLeague.py
echo "success!"
sleep 2

echo "saving data..."
cd ../saveData/ && python3 savePLData.py
echo "success!"
sleep 2

echo "printing data..."
cd ../calcOdds && python3 calcPL.py
