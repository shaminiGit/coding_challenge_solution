#!/bin/bash
#!/usr/bin/env bash
# load dependancies
apt-get update
apt-get install python3.8 

# set proper permissions
chmod a+x ./src/consumer_complaints.py


# execute scripts
python3 ./src/consumer_complaints.py ./input/complaints.csv ./output/report.txt
