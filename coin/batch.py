# -*- coding: utf-8 -*-
import ftplib
import sendMail
import time
from shutil import copyfile
import configparser

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['godaddy.url']
gduser = config['godaddy']['godaddy.user']
gdpass = config['godaddy']['godaddy.pass']

url = config['yahoo']['yahoo.url']
user = config['yahoo']['yahoo.user']
password = config['yahoo']['yahoo.pass']
server = config['yahoo']['yahoo.server']
port = config['yahoo']['yahoo.port']
username = config['yahoo']['yahoo.username']

exec(open("C:\\dep\\Mechanizd\\coin\\market.py").read())

timestr = time.strftime("%Y%m%d_%H%M%S")

session = ftplib.FTP(gdurl,gduser,gdpass)

theFile = 'C:\\dep\\Mechanizd\\coin\\btcmktcap.htm'

copyfile(theFile, 'C:\dev\godaddy\\mech\output\Bitcoin\\btcmktcap.htm')
    
file = open(theFile,'rb')
session.storbinary('STOR /mech/output/Bitcoin/btcmktcap.htm', file)
file.close()
        
with open(theFile, 'r') as f:
    data = str(f.read())
    sendMail.send_mail('jrathgeber@yahoo.com', 'jrathgeber@yahoo.com', 'BTC Mkt Cap', data, [], server, port, username, password)
    
session.quit()    

