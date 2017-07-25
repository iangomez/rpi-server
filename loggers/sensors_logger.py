#!/usr/bin/python3
# Sensor logger
# july 23, 2017
# ian gomez

import smartpi

# read data
cpu = smartpi.read_cpu()
T = smartpi.read_temp()[1]
humidity = smartpi.read_temp()[0]

# add sensor data
add_data = ("INSERT INTO sensors"
	"(dt, cpu, dht1_T, dht1_hum)"
	"VALUES (NOW(), %s, %s, %s)")
data = (cpu, T, humidity)
smartpi.add2msql(add_data, data)

print("temp={}F, humidity={}%".format(T, humidity))
