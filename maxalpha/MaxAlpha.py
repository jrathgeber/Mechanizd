# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:51:41 2019

@author: Jason
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:50:56 2018

@author: Jason
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time
#import Pg

#import configparser

def parseWebSite(daterun):
    
    #config = configparser.ConfigParser()
    #config.read('C:\etc\properties.ini') 

    maurl = 'https://secure.trade-ideas.com/cms_static/kathy_test/tivision/TradeIdeasVision.php?cloud_code=cbf36ff3ba1990a750ce63b90f22aa50&height=700&width=848'    

    
    print('hello1') 

    browser=webdriver.Firefox()

    print('hello2') 

    browser.get(maurl)

    #time.sleep(15)
    time.sleep(7)    
    
    print('hello3')    
    
    soup=BeautifulSoup(browser.page_source, "lxml")
    
    #print(soup)    
    
    data = []
    
    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
        
        
    #print (len(data))      
    #print(data[50][0])
    #print(data)
    
    # Adda a stock here
    juno = []    
    
    if data[45][0]!='No Stocks On WatchThe Max Alpha Watch List is only active on weekdays starting at 4AM EST': 
        
        print (len(data))    
    
        #Pg.pgInsert(data)
    
        watchitems = len(data)    

        if len(data)>0:
            
            for x in range(6, watchitems):
        
                if len(data[x])>9:
                              
                    ticker_ok= False    
                    price_ok= False
                    gain_ok= False
                    volume_ok= False    
                    #events_ok= False 
                                
                    # these tickers cause problems
                    if(data[x][0] not in ['USAU', 'NA', 'YERR', 'TVIX', 'MLPO']):
                        ticker_ok=True    
        
                    #print (len(data[x]))    
                    #print(data[x])
                 
                    num = data[x][1]            
                    if(float(num.replace("$", "")) <= 12.0):
                        price_ok=True    
        
                    if(float(num.replace("$", "")) <= 1.00):
                        price_ok=False
        
                    gap = data[x][4]
                    if(float(gap.replace(",", "").replace("M", "")) >= 10):
                        gain_ok=True    
        
                    vol = data[x][5]  
                    if(float(vol.replace(",", "").replace("M", "")) >= 3):
                        volume_ok=True    
        
                    #string news = data[x][5]
                    #if(['Buy-out', 'Merger'] not in news):
                    #    events_ok=True    
        
                    if(ticker_ok and price_ok and gain_ok and volume_ok):
                        juno.append(data[x][0])        
        
    
        #else:
        #    juno = ['CARA', 'VIPS']
        #print(juno)    
    
    #browser.close()
    
    return juno
    
daterun = time.strftime("%Y%m%d")
parseWebSite(daterun)