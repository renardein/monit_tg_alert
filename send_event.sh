#!/bin/bash
date=$(date '+%H:%M:%S %d-%m-%Y')
/mnt/monit/monit_alert.py -c "-100131212" -t 10 -m "Host $MONIT_SERVICE is online now"
