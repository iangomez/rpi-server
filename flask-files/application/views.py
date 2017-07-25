from flask import render_template, flash, redirect
from application import app
import matplotlib.pyplot as plt


# Index
#-------------------------------------------------------------------------------
@app.route('/') # a decorator
@app.route('/index')
def index():
    return build_plot()

def build_plot_weather():
    table = 'weather'
    data  = 'dt, zone, temp_f, feelslike_f, wind_mph, UV'
    rows = fetch_data(table, data)
    return print(rows)

def fetch_data(table, data):
	cnx = mysql.connector.connect(user='ian',password=keys.password,
		host='localhost',database='homeautomation')
	cursor = cnx.cursor()
    get_data = 'SELECT {} FROM {}'.format(data_want, table_want)
    cursor.execute(get_data)
    rows = cursor.fetchall()
	cursor.close()
	cnx.close()
    return rows
