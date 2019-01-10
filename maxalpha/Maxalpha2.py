# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:50:56 2018

@author: Jason
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time
import Pg

import configparser

def parseWebSite(daterun):
    
    config = configparser.ConfigParser()
    config.read('C:\etc\properties.ini') 
    
    maurl = config['maxalpha']['url']
    mauser = config['maxalpha']['user']
    mapass = config['maxalpha']['pass']

    browser=webdriver.Firefox()
    browser.get(maurl+'/login')
    #browser.get('http://maxalpha.co/login')    
    
    username = browser.find_element_by_id("email_address")
    password = browser.find_element_by_id("password")
    
    username.send_keys(mauser)
    password.send_keys(mapass)
    password.send_keys(Keys.RETURN);

    time.sleep(6)
    #time.sleep(60)    
    
    soup=BeautifulSoup(browser.page_source, "lxml")
    
    table_body = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="watchlist") 
    
    data = []
    
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
        
    print(data[1][0])
    
    # Adda a stock here
    juno = []    
    
    if data[1][0]!='No Stocks On WatchThe Max Alpha Watch List is only active on weekdays starting at 4AM EST': 
        
        print (len(data))    
    
        #Pg.pgInsert(data)
    
        watchitems = len(data)    

        if len(data)>0:
            
            for x in range(1, watchitems):
                                      
                ticker_ok= False    
                price_ok= False
                gain_ok= False
                volume_ok= False    
                #events_ok= False 
                            
                # these tickers cause problems
                if(data[x][0] not in ['USAU', 'NA', 'YERR', 'TVIX']):
                    ticker_ok=True    
    
                #print(data[:])
             
                num = data[x][2]            
                if(float(num.replace("$", "")) <= 12.0):
                    price_ok=True    
    
                if(float(num.replace("$", "")) <= 1.00):
                    price_ok=False
    
    
                if(float(data[x][3]) >= 10):
                    gain_ok=True    
    
                vol = data[x][5]  
                if(float(vol.replace(",", "")) >= 30000):
                    volume_ok=True    
    
                #string news = data[x][5]
                #if(['Buy-out', 'Merger'] not in news):
                #    events_ok=True    
    
                if(ticker_ok and price_ok and gain_ok and volume_ok):
                    juno.append(data[x][0])        
    
    
        else:
            juno = ['AXSM', 'VIPS']
        print(juno)    
    
    browser.close()
    
    return juno
