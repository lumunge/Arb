#!/bin/bash

echo "clearing json files..."
cd json/LLJson/ && rm -rf *
echo "success!"
sleep 2

echo "clearing tables..."
cd ../../database/ && python3 clearLlTables.py
echo "success!"
sleep 2

echo "fetching data..."
cd ../fetchData/ && python3 fetchLaliga.py
echo "success!"
sleep 2

echo "saving data..."
cd ../saveData/ && python3 saveLL.py
echo "success!"
sleep 2

echo "printing data..."
cd ../calcOdds && python3 calcLL.py
 