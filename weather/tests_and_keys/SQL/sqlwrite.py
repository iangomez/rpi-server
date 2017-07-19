#!/usr/bin/env python3
# SQLwrite	
# ian gomez
# july 16, 2017

import mysql.connector
import random
import time
from datetime 

# open SQL
db = mysql.connector.connect(user='monitor',password='pswd', 
	host='localhost', database='temps')
curs = db.cursor()

# set up parameters to store
today = datetime.now().date()
time_str  = time.strftime("%H:%M:%S")
zone = 'Alhambra'
T = random.randrange(60,100)

# MySQL code to store temperature
add_temp = ("INSERT INTO tempdat "
			"(tdate, ttime, zone, temperature) "
			"VALUES (%s, %s, %s, %s)")
data_temp = (today, time_str, zone, T)
curs.execute(add_temp, data_temp)
db.commit()

# close MySQL
curs.close()
db.close()