# -*- coding: utf-8 -*-
#/usr/bin/pythonzzzz
#
#

# load the adapter
import psycopg2

# load the psycopg extras module
import psycopg2.extras

# Try to connect

try:
    conn=psycopg2.connect("dbname='rambo' user='postgres' password='postgres'")
except:
    print ('I am unable to connect to the database.')

# If we are accessing the rows via column name instead of position we 
# need to add the arguments to conn.cursor.

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cur.execute("""SELECT * from jhi_user""")
except:
    print ("I can't SELECT from bar")

#
# Note that below we are accessing the row via the column name.

rows = cur.fetchall()
for row in rows:
    print ("   ", row['login'])

