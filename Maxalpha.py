# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:50:56 2018

@author: Jason
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time

import configparser


def parseWebSite(daterun):
        
    config = configparser.ConfigParser()
    config.read('C:\etc\properties.ini') 
    
    maurl = config['maxalpha']['url']
    mauser = config['maxalpha']['user']
    mapass = config['maxalpha']['pass']

    browser=webdriver.Firefox()
    browser.get(maurl)
 
    browser.get(maurl+'/login')    
    username = browser.find_element_by_id("email_address")
    password = browser.find_element_by_id("password")
    
    username.send_keys(mauser)
    password.send_keys(mapass)
    password.send_keys(Keys.RETURN);

    time.sleep(120)
    
    soup=BeautifulSoup(browser.page_source, "lxml")
    
    table_body = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="watchlist") 
    
    data = []
    
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
        
    print(data[1][0])
    
    print (len(data))    

    watchitems = len(data)    
    
    juno = []
    
    if len(data)>0:
        
        for x in range(1, watchitems):
            if(data[x][0] not in ['USAU', 'NA']):
                juno.append(data[x][0])        

    else:
        juno = ['error']
    print(juno)    
    
    browser.close()
    
    return juno
    
