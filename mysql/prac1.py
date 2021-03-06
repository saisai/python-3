#!/usr/bin/env python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "password", "playground")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# execute another SQL query
cursor.execute("SELECT * FROM equipment")

# Fetches all rows using fetchall() method.
data = cursor.fetchall()
print data
print type(data)
#print "Database version: %s " % data

# disconnect from server
db.close()
