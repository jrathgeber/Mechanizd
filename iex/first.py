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



a = Stock("AAPL", token=key)
print(a.get_quote())