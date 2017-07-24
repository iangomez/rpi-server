#!/usr/bin python3
# Create MySQL databases
# ian gomez
# July 23, 2017

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import keys
import mysql.connector

db_name = "home-automation"
table_names = ["weather", "pinfo", "sensors"]

# open mysql
cnx = mysql.connector.connect(user='ian',password=keys.password)
cursor = cnx.cursor()

try:
    print("Creating database {}: ".format(db_name), end='')
    cursor.execute(
        "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)
else:
    print("OK\n")

# weather table
table_weather = ("CREATE TABLE weather ("
	"dt DATETIME,"
    "zone TEXT,"
	"temp_f DECIMAL(4,1),"
	"feelslike_f DECIMAL(4,1),"
	"wind_mph DECIMAL(4,1),"
	"UV INT(2)"
	")")

table_pi = ("CREATE TABLE pinfo ("
    "cpu"
