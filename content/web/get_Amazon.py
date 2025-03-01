# -*- coding: utf-8 -*-
"""

Created on Wed Jan  3 21:50:56 2019

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

    # maurl = 'https://secure.trade-ideas.com/cms_static/kathy_test/tivision/TradeIdeasVision.php?cloud_code=cbf36ff3ba1990a750ce63b90f22aa50&height=700&width=848'

    maurl = "https://www.amazon.com/40-Week-Ironman-Step-Step-Conquering/dp/B0C5P9WYFT/?_encoding=UTF8&pd_rd_w=PuCFj&content-id=amzn1.sym.117cb3e1-fd12-46a0-bb16-15cd49babfdb%3Aamzn1.symc.abfa8731-fff2-4177-9d31-bf48857c2263&pf_rd_p=117cb3e1-fd12-46a0-bb16-15cd49babfdb&pf_rd_r=SJF9NRD53N8HBPARJ7SK&pd_rd_wg=ZOtEk&pd_rd_r=03b9aa61-afb0-4bf4-842c-d12c3816e4eb&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d"

    browser=webdriver.Firefox()
    browser.get(maurl)
    time.sleep(7)    

    soup=BeautifulSoup(browser.page_source, "lxml")

    print(soup.text)

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
        
        #print (len(data))    
    
        #Pg.pgInsert(data)
    
        watchitems = len(data)    

        if len(data)>0:
            
            for x in range(5, watchitems):
        
                if len(data[x])>7:
                              
                    ticker_ok= False    
                    price_ok= False
                    gain_ok= False
                    volume_ok= False    
                    #events_ok= False 
                                
                    # these tickers cause problems
                    if(data[x][0] not in ['USAU', 'NA', 'YERR', 'TVIX', 'MLPO', 'AZO']):
                        ticker_ok=True    
        
                    #print (len(data[x]))    
                    #print(data[x])
                 
                    num = data[x][1]            
                    if(float(num.replace("$", "").replace(",", "")) <= 10.0):
                        price_ok=True    
        
                    if(float(num.replace("$", "").replace(",", "")) <= 1.00):
                        price_ok=False
        
                    # Gap
                    if(len(data[x])==12):
                        gap = data[x][4]
                        vol = data[x][5]
                    elif(len(data[x])==11):
                        gap = data[x][4]
                        vol = data[x][5]                        
                    elif(len(data[x])==10):
                        gap = data[x][4]
                        vol = data[x][5]
                    elif(len(data[x])==9):
                        gap = data[x][4]
                        vol = data[x][5]                         
                    #elif(len(data[x])==8):
                    #    gap = data[x][3]
                    #    vol = data[x][4]                         
                    else :
                        gap = data[x][4]
                        vol = data[x][5]                  
               
                    # conditional gets
                    gap_mult = 1
                    if ('M' in gap):
                        gap_mult = 1000000
                    if ('K' in gap):
                        gap_mult = 1000    
                    if(float(gap.replace(",", "").replace("M", "").replace("K", "")) * gap_mult >= 10):
                        gain_ok=True    
        
                    # Vol
                    vol_mult = 1
                    if ('M' in vol):
                        vol_mult = 1000000
                    if ('K' in gap):
                        vol_mult = 1000                    
                    if(float(vol.replace(",", "").replace("M", "").replace("K", "")) * vol_mult >= 10000):
                        volume_ok=True    

                    #print(data[x][0] + ' ' + vol.replace(",", "").replace("M", "") + " " + gap.replace(",", "").replace("M", "") )        
                    #print('' + str(ticker_ok) + ' ' + str(price_ok) + ' ' + str(gain_ok) + ' ' + str(volume_ok))


                    #string news = data[x][5]
                    #if(['Buy-out', 'Merger'] not in news):
                    #    events_ok=True    
        
                    if(ticker_ok and price_ok and gain_ok and volume_ok):
                        juno.append(data[x][0])        
        
    
        # else:
        #    juno = ['CARA', 'VIPS']
        # print(juno)    
    
    browser.close()
    
    return juno
    
daterun = time.strftime("%Y%m%d")
parseWebSite(daterun)