# -*- coding: utf-8 -*-

import os;
import time;
import SymbolConfig as SC;


os.chdir('C:\\dep\Mechanizd\\maxalpha\\')

daterun = time.strftime("%Y%m%d")
daterun = "20210528"

print('Date ' +  daterun)

maxdata='hello'
   
tickerList = ['GME', 'AMC', 'TSLA', 'VTNR']
print('Ticker List : ')
print(tickerList)

# Test It
SC.getSymbolConfig(tickerList, daterun, maxdata)

