#!/bin/bash

echo "clearing json files..."
cd json/SAJson/ && rm -rf *
echo "success!"
sleep 2

echo "clearing tables..."
cd ../../database/ && python3 clearSaTables.py
echo "success!"
sleep 2

echo "fetching data..."
cd ../fetchData/ && python3 fetchSerieA.py
echo "success!"
sleep 2

echo "saving data..."
cd ../saveData/ && python3 saveSerie.py
echo "success!"
sleep 2

echo "printing data..."
cd ../calcOdds && python3 calcSA.py