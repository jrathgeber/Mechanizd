# -*- coding: utf-8 -*-

import os;
import RightEdge as RE;
import Maxalpha2 as MA;
import time;
import sendMail;
import SymbolConfig as SC;
import threading;
import configparser

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['url']
gduser = config['godaddy']['user']
gdpass = config['godaddy']['pass']

url = config['yahoo']['url']
user = config['yahoo']['user']
password = config['yahoo']['pass']
server = config['yahoo']['server']
port = config['yahoo']['port']
username = config['yahoo']['username']

os.chdir('C:\dep\maxalpha\\')

daterun = time.strftime("%Y%m%d")

print(daterun)

closeup = '/E'
get_prices = '/U'
mode = '/L'

#maxdata=["The", "earth", "revolves", "around", "sun"]
maxdata='hello'

def MyThread1():
    RE.runRightEdge('MaxAlphaMinShort', 'MaxAlpha', 'MaxAlpha', mode, '/'+ daterun, get_prices, closeup)
    
    
tickerList = MA.parseWebSite(daterun);

if tickerList[0]=='error':
    sendMail.send_mail('jrathgeber@yahoo.com', 'jrathgeber@yahoo.com', 'Max List Eorror ' + ''.join(tickerList), ''.join(tickerList))
else:

    SC.getSymbolConfig(tickerList, daterun, maxdata)
    sendMail.send_mail(user, user, 'Max ' + ''.join(tickerList), ''.join(tickerList)[], server, port, username, password)
    t1 = threading.Thread(target=MyThread1)
    t1.start()

#    
