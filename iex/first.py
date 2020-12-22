# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:17:42 2020

@author: Jason
"""

from iexfinance.stocks import Stock

import configparser

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

key = config['iex']['iex.secretkey']



a = Stock("APRN", token=key)

print(a.get_quote())
#print(a.get_balance_sheet())


aapl = Stock("AAPL", token=key)

#print(aapl.get_company_name())

#print(aapl.get_key_stats())


def getAllPrices(tickerlist):
    
        batch = Stock(tickerlist, token=key)
        batch.get_price()
        
        return batch
    
        
#print(getAllPrices(["TSLA", "AAPL"]))
