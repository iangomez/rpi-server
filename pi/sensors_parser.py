#!/usr/bin/python3
# Sensor logger
# july 23, 2017
# ian gomez

import mysql.connector
import keys
import pit

# open database
cnx = mysql.connector.connect(user='ian',password=keys.password,
	host='localhost',database='homeautomation')
cursor = cnx.cursor()

# add data
add_data = ("INSERT INTO pinfo"
	"(dt, dht1_T, dht1_hum)"
	"VALUES (NOW(), %s, %s, %s)")
data = (pit.read_cpu(), pit.read_temp()[1], pit.read_temp()[0])
cursor.execute(add_data,data)
cnx.commit()

# close connection
cursor.close()
cnx.close()
