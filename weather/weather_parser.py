#!/usr/bin/env python3
# Weather logger
# july 15, 2017
# ian gomez

# cron commands for runninig every half hour
# crontab -e
# */30 * * * * /usr/bin/python3 /home/pi/weather/weather_parser.py

import keys
import requests
import datetime
import mysql.connector
from pushbullet import Pushbullet

notifyme = 0

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

# open database
cnx = mysql.connector.connect(user='ian',password=keys.password,
	host='localhost',database='weatherdb')
cursor = cnx.cursor()

# add data
add_data = ("INSERT INTO weather"
	"(dt, zone, temp_f, feelslike_f, wind_mph, UV)"
	"VALUES (NOW(), %s, %s, %s, %s, %s)")
data = (city,temp_f,feelslike_f,wind_mph,uv)
cursor.execute(add_data,data)
cnx.commit()

# close connection
cursor.close()
cnx.close()

# set up api call for pushbullet
if notifyme == 1:
	log = str(city) + ", " + str(temp_f) + ", " + str(wind_mph)
	pb = Pushbullet(keys.pbapi)
	push = pb.push_note('Weather Update', log)
