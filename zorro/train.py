# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 06:52:28 2017

@author: Jason
"""

from subprocess import Popen

zorro_path = 'F:\\Zorro\\Gain_19x\\'
assets = ["EUR/USD", "GBP/USD", "AUD/USD", "NZD/USD", "USD/CHF", "USD/JPY"]
begin = 2010
end = 2018
directive = 'NO'
strategy = 'J12'


models = ('downloadj','J12')
#models = ('downloadj','J12','J12a','J12b','J12c')

for model in models:

    j12 = [r"F:\\Zorro\\Zorro_19X\\Zorro.exe", "-train", model, "-c" , "J1"]
    j12_prog = Popen(j12)
   
    stdout, stderr = j12_prog.communicate()