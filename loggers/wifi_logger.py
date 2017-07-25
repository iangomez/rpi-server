#!/usr/bin/python3
# Wifi logger
# july 24, 2017
# ian gomez

import keys
import subprocess
import smartpi
from pushbullet import Pushbullet
pb = Pushbullet(keys.pbapi)

# read wifi info
output = subprocess.check_output(["speedtest-cli --simple"], shell=True)
listout = output.split()
ping = float(listout[1])
down = float(listout[4])
up   = float(listout[7])

# add wifi data
add_data = ("INSERT INTO wifi"
	"(dt, ping, down, up)"
	"VALUES (NOW(), %s, %s, %s)")
data = (ping, down, up)
smartpi.add2msql(add_data, data)

push = pb.push_note('Wifi', 'ping: {}ms, down: {}mb/s, up: {}mb/s'.format(ping, down, up))

