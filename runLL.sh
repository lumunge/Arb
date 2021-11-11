#!/bin/bash

echo "clearing json files..."
cd JSON/LLJson/ && rm -rf *
echo "success!"
sleep 2

echo "clearing tables..."
cd ../../DBS/ && python3 clearLlTables.py
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
cd ../ && python3 calcLL.py
 