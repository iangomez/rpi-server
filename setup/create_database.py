#!/usr/bin/python3
# Create homeautomation MySQL database
# ian gomez
# July 23, 2017

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import keys
import mysql.connector

cnx = mysql.connector.connect(user='ian',password=keys.password)
cursor = cnx.cursor()

# make database
db_name = "homeautomation"
try:
    print("Creating database {}: ".format(db_name), end='')
    cursor.execute(
        "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)
else:
    print("OK\n")

# weather and sensors tables
table_weather = ("CREATE TABLE weather ("
	"dt DATETIME,"
    "zone TEXT,"
    "temp_f DECIMAL(5,2),"
    "feelslike_f DECIMAL(5,2),"
	"wind_mph DECIMAL(5,1),"
    "UV INT(2))")
table_sensors = ("CREATE TABLE sensors ("
	"dt DATETIME,"
    "cpu DECIMAL(8,2),"
    "dht1_T DECIMAL(5,2),"
    "dht1_hum DECIMAL(5,2))")
table_wifi = ("CREATE TABLE wifi ("
    "dt DATETIME,"
    "ping DECIMAL(5,2)"
    "down DECIMAL(5,2)"
    "up DECIMAL(5,2))")

# make the tables
table_names = ["weather", "sensors", "wifi"]
tables = [table_weather, table_sensors]
for table, table_name in zip(tables, table_names):
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute('USE {}'.format(db_name))
        cursor.execute(table)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK\n")

cursor.close()
cnx.close()
