# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:41:28 2018

@author: Jason
"""

#import os;
#import RightEdge as RE;
#import Maxalpha2 as MA;
#import Optimise as OP;
#import time;
#import SymbolConfig as SC;

#os.chdir('C:\dep\\Mechanizd\\maxalpha\\')
#daterun = time.strftime("%Y%m%d")
#OP.optimise('MaxAlpha')

import os;
import RightEdge as RE;
import MaxAlpha as MA;
import time;
import sendMail;
import SymbolConfig as SC;
import threading;
import configparser
import Tweet
#import iex.first as IEX

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

os.chdir('C:\\dep\Mechanizd\\maxalpha\\')

daterun = time.strftime("%Y%m%d")

#print(daterun)

closeup = '/E'
get_prices = '/U'
#get_prices = ''
mode = '/L'

#maxdata=["The", "earth", "revolves", "around", "sun"]
maxdata='hello'


#tickerList = ['AXSM', 'VIPS']    
tickerList = MA.parseWebSite(daterun);
print(tickerList)
#allpriceslist = IEX.getAllPrices(tickerList)
print(allpriceslist)