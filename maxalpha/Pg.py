# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#/usr/bin/pythonzzzz
#


# load the adapter
import psycopg2

# load the psycopg extras module
import psycopg2.extras

#config
import configparser

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

dbname = config['postgres']['url']
dbuser = config['postgres']['user']
dbpass = config['postgres']['pass']


def pgInsert(data):

    # Try to connect
    try:
        conn=psycopg2.connect("dbname='"+dbname+"' user='"+dbuser+"' password='"+dbpass+"'")
    except:
        print ('I am unable to connect to the database.')
    
    # If we are accessing the rows via column name instead of position we 
    # need to add the arguments to conn.cursor.
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur = conn.cursor()
    
    try:
        cur.execute("""SELECT * from maxalpha.max""")

    except:
        print ("I can't SELECT from bar")
    
    # Note that below we are accessing the row via the column name.
    rows = cur.fetchall()
    for row in rows:
        print (" Hi  ", row[1])
   
    
    watchitems = len(data)    
      
    if len(data)>0:
        
        for x in range(1, watchitems):
            
            symbol  = data[x][0]
            timea   = data[x][1]
            price   = data[x][2].replace("$", "")            
            change  = data[x][3]
            net     = data[x][3]             
            volume  = data[x][5].replace(",", "")                
            recent  = data[x][6] 
            
            related = ''
            if len(data[x])>7:        
                related = data[x][7]
            
            s = """UPSERT INTO maxalpha.max("Date_Added", "Symbol", "Time_Added", "Last_Price", "Percent_Change", "Net_Change", "Volume", "Recent_Events", "Related_Data") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cur.execute(s,('now()', symbol , 'now()', price , change, net, volume, recent, related))
            conn.commit() # <- We MUST commit to reflect the inserted data
    
    cur.close()
    conn.close()