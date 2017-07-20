#!/usr/bin/env python3

import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import datetime
import keys

cnx = mysql.connector.connect(user='ian',password=keys.password,
	host='localhost',database='weatherdb')
cursor = cnx.cursor()
cursor.execute("SELECT dt, zone, temp_f, feelslike_f, wind_mph, uv FROM weather")
rows = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'dtime', 1: 'Zone', 2: 'Temp (F)', 3: 'Feels like (F)',
    4:'Wind (mph)', 5:'UV'}, inplace=True);
df = df.sort(['dtime'], ascending=[1]);

x=df['dtime']
y=df['Temp (F)']

plt.plot(x,y)
plt.show()

