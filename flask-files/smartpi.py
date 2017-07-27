#!/usr/bin/python3

from flask import Flask
import matplotlib.pyplot as plt
import mysql.connector
import keys

# specify app
app = Flask(__name__)
app.config.from_object('config')
dmode = True # set debug mode

################################################################################
# Views                                                                        #
################################################################################

# Index
@app.route('/') # a decorator
@app.route('/index')
def index():
    return build_plot_weather()

################################################################################
# Helper Functions                                                             #
################################################################################

def build_plot_weather():
    table = 'weather'
    data  = 'dt, zone, temp_f, feelslike_f, wind_mph, UV'
    rows = fetch_data(data, table)

    # parse data into arrays for plotting

    img = io.BytesIO()
    plt.plot(x,y)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plot_url)

# general fetch function
def fetch_data(data, table):
    cnx = mysql.connector.connect(user='ian',password=keys.password,
    	host='localhost',database='homeautomation')
    cursor = cnx.cursor()

    get_data = 'SELECT {} FROM {}'.format(data, table)

    cursor.execute(get_data)
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()

    return rows

if __name__ == "__main__":
    app.run(debug=dmode)
