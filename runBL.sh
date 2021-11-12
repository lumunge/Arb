#!/bin/bash

cd JSON/BLJson/ && rm -rf *
echo "cleared json success!"
sleep 2

cd ../../DBS/ && python3 clearBlTables.py
echo "cleared tables success!"
sleep 2

cd ../fetchData/ && python3 fetchBundesliga.py
echo "fetched data success!"
sleep 2

cd ../saveData/ && python3 saveBL.py
echo "saved data success!"
sleep 2

echo "printing data..."
cd ../ && python3 calcBL.py