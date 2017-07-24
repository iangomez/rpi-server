#!/usr/bin/python3
# Weather logger
# july 15, 2017
# ian gomez

import keys
import requests
import datetime
import smartpi

# get data from wunderground
state = 'CA'
city = 'Alhambra'
urlData = ('http://api.wunderground.com/api/' +
	keys.wuapi+'/geolookup/conditions/q/{}/{}.json'.format(state, city))
jsonData = requests.get(urlData).json()

# parse the json file
temp_f = jsonData['current_observation']['temp_f']
feelslike_f = jsonData['current_observation']['feelslike_f']
wind_mph = jsonData['current_observation']['wind_mph']
uv = jsonData['current_observation']['UV']

# add data
add_data = ("INSERT INTO weather"
	"(dt, zone, temp_f, feelslike_f, wind_mph, UV)"
	"VALUES (NOW(), %s, %s, %s, %s, %s)")
data = (city, temp_f, feelslike_f, wind_mph, uv)
smartpi.add2msql(add_data, data)
