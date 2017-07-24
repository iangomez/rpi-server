#!/usr/bin/python3
# Pi Telemetry
# Ian Gomez with special thanks to Davy Ragland
# July 23, 2017

import subprocess
import Adafruit_DHT

# Function: read_cpu (Davy Ragland)
# This function reads the percent memory used by the CPU.
def read_cpu():
	output = subprocess.check_output(
		["grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"],
		 shell=True)
	cpu_use = float(output[2:6])
	return cpu_use

# Function: read_memory (Davy Ragland)
# This function reads the percent memory available on the raspberry pi.
def read_memory():
	output = subprocess.check_output(
		["df -h | grep /dev/root | cut -d ' ' -f 14-"],
		shell=True)
	mem_use = float(output[7:8])/100.0 # can't parse correctly
	return mem_use

# Function: read_temp
# Reads the DHT22 temperature sensor connected to the specified pin
def read_temp():
	sensor = Adafruit_DHT.DHT22
	pin_T = 22
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_T)
	return humidity, temperature
