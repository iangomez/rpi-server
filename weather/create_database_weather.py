#!/usr/bin python3
# Create MySQL database for weather
# ian gomez
# July 19, 2017

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import keys
import mysql.connector

# setup names for your mysql objects
db_name = 'weatherdb'
table_name = 'weather'

# open mysql
cnx = mysql.connector.connect(user='ian',password=keys.password)
cursor = cnx.cursor()

# make the database if it doesn't exist
try:
    print("Creating database {}: ".format(db_name), end='')
    cursor.execute(
        "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)
else: 
    print("OK\n")

# edit to make whatever type and size of table you want
make_table = ("CREATE TABLE {} ("
	"dt DATETIME,"
    "zone TEXT,"
	"temp_f DECIMAL(4,1),"
	"feelslike_f DECIMAL(4,1),"
	"wind_mph DECIMAL(4,1),"
	"UV INT(2)"
	")").format(table_name)

# make the table if it doesn't already exist
try:
    print("Creating table {}: ".format(table_name), end='')
    cursor.execute('USE {}'.format(db_name))
    cursor.execute(make_table)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
    else:
        print(err.msg)
else:
    print("OK\n")
