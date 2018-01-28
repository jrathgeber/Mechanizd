# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:50:56 2018

@author: Jason R
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time


def parseWebSite(daterun):

    browser=webdriver.Firefox()
    browser.get('https://maxalpha.co')
    
    time.sleep(5)
    
    soup=BeautifulSoup(browser.page_source, "lxml")
    
    table_body = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="watchlist") 
    
    data = []
    
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
        
    print(data[1][0])
    
    print (len(data))    

    watchitems = len(data)    
    
    watchlist = []
    
    if watchitems>0:
        
        for x in range(1, watchitems):
            watchlist.append(data[x][0])        

    else:
        watchlist = ['error']
    print(watchlist)    
    
    browser.close()
    
    return watchlist
    
