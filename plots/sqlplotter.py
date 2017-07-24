#!/usr/bin/env python3

# SQL Plotter
# Ian Gomez
# July 20, 2017

import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import datetime
import keys
from numpy import arange
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange


# open MySQL and fetch all data 
cnx = mysql.connector.connect(user='ian',password=keys.password,
	host='localhost',database='weatherdb')
cursor = cnx.cursor()
cursor.execute("SELECT dt, zone, temp_f, feelslike_f, wind_mph, uv FROM weather")
rows = cursor.fetchall()

# place in dataframe for easier manipulation
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'dtime', 1: 'Zone', 2: 'Temp (F)', 3: 'Feels like (F)',
    4:'Wind (mph)', 5:'UV'}, inplace=True);
df = df.sort(['dtime'], ascending=[1]);

# use variables for simple plotting
dt = df['dtime']
temp_f = df['Temp (F)']
feelslike_f = df['Feels like (F)']

# plot
plt.plot(dt,temp_f, label="absolute")
plt.plot(dt,feelslike_f, label="feels like")
plt.xlabel('time')
plt.ylabel('Temperature (F)')
plt.title('Temperature in Alhambra')
plt.legend()
plt.show()
