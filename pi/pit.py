#!/usr/bin/python3
# Pi Telemetry
# Ian Gomez with special thanks to Davy Ragland 
# July 23, 2017

import Adafruit_DHT

# Function: read_cpu (Davy Ragland)
# This function reads the percent memory used by the CPU.
def read_cpu():
	output = subprocess.check_output(
		["grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"],
		 shell=True)
	config.cpu = str(output)[:2]
	print(str(output)[:2])

# Function: read_memory (Davy Ragland)
# This function reads the percent memory available on the raspberry pi.
def read_memory():
	output = subprocess.check_output(
		["df -h | grep /dev/root | cut -d ' ' -f 14-"], 
		shell=True)
	config.memory = str(output)[:2]
	print(str(output)[:2])

# Function: read_temp
# Reads the DHT22 temperature sensor connected to the specified pin
def read_temp():
	sensor = Adafruit_DHT.DHT22
	pin_T = 22
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
    	print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
	else:
    	print('Failed to get reading. Try again!')
