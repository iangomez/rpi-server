#!/usr/bin/env python3

from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='ian', password='CNKlibrary', host='localhost', database='employees')
cursor = cnx.cursor()

cursor.execute((
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB"))

cursor.close()
cnx.close()