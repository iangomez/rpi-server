#!/usr/bin/env python3
# SQLread
# ian gomez
# july 18, 2017

import mysql.connector
import time
from datetime

# open SQL
db = mysql.connector.connect(user='monitor',password='pswd',
	host='localhost', database='temps')
curs = db.cursor()

data_get = 'SELECT tdate, ttime, temperature FROM tempdat'

curs.execute(data_get)
rows = curs.fetchall()

x = []; data = []
for row in rows:
	x.append(row[1])
	data.append(row[2])

curs.close()
db.close()

print(x)
print(data)
