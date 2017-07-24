#!/usr/bin/python3
# Sensor logger
# july 23, 2017
# ian gomez

import mysql.connector
import keys
import smartpi

# open database
cnx = mysql.connector.connect(user='ian',password=keys.password,
	host='localhost',database='homeautomation')
cursor = cnx.cursor()

# read data
cpu = smartpi.read_cpu()
T = smartpi.read_temp()[1]
humidity = smartpi.read_temp()[0]

# add sensor data
add_data = ("INSERT INTO sensors"
	"(dt, cpu, dht1_T, dht1_hum)"
	"VALUES (NOW(), %s, %s, %s)")
data = (cpu,T,humidity)
cursor.execute(add_data, data)
cnx.commit()

# close connection
cursor.close()
cnx.close()
