#!/bin/bash

echo "clearing json files..."
cd jsonFiles && python3 clearJson.py
echo "success!"
sleep 2

echo "clearing tables..."
cd .. && python3 clearTables.py
echo "success!"
sleep 2

echo "fetching data..."
python3 fetchData.py
echo "success!"
sleep 2

echo "saving data..."
python3 saveData.py
echo "success!"
sleep 2

echo "printing data..."
python3 calc.py
