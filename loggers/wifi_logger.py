#!/usr/bin/python3
# Wifi logger
# july 24, 2017
# ian gomez

import mysql.connector
import keys

# open database
cnx = mysql.connector.connect(user='ian',password=keys.password,
	host='localhost',database='homeautomation')
cursor = cnx.cursor()

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
data = (ping,down,up)
cursor.execute(add_data, data)
cnx.commit()

# close connection
cursor.close()
cnx.close()
