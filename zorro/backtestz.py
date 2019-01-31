# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 06:52:28 2017

@author: Jason
"""

from subprocess import Popen

import ftplib
import time
from shutil import copyfile

import os;
os.chdir('C:\\dep\\Mechanizd\\batch\\')

import FileReadingBackTest as FR

import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['url']
gduser = config['godaddy']['user']
gdpass = config['godaddy']['pass']

timestr = time.strftime("%d%m%y")
session = ftplib.FTP(gdurl,gduser,gdpass)

models = ('Z1','Z2','Z12','Z7')
#models = ('Z7',)

fileTypes = ('.htm','.txt', '_pnl.csv', '_Test.log')

for model in models:

    j12 = [r"F:\\Zorro\\Zorro_19X\\Zorro.exe", "-run", model, "-c" , "J1"]
    j12_prog = Popen(j12)
    stdout, stderr = j12_prog.communicate()
    
    if model != 'downloadj' :

        for fileType in fileTypes:

            copyfile('F:\Zorro\\Zorro_19X\Log\\' + model + fileType, 'C:\dev\godaddy\\mech\\output\Zorro\\Testz\\' + model + '_' + timestr + fileType)
            
            file = open('F:\Zorro\\Zorro_19X\Log\\' + model + fileType,'rb')
            session.storbinary('STOR /mech/output/Zorro/Testz/' + model + '_' + timestr + fileType, file)
            file.close()
    
        copyfile('F:\Zorro\\Zorro_19X\Log\\Testtrades.csv', 'C:\dev\godaddy\\mech\\output\Zorro\\Testz\\' + model + '_' + timestr + '_Testtrades.csv')    
        
        file = open('F:\Zorro\\Zorro_19X\Log\\Testtrades.csv','rb')
        session.storbinary('STOR /mech/output/Zorro/Testz/' + model + '_' + timestr + '_testtrades.csv', file)
        file.close()    
    

FR.fileReading("C:\dev\godaddy\\mech\output\Zorro\\Testz\\Z*.txt", 'C:\dev\godaddy\\mech\output\Zorro\Testz\ZorroResults.htm', 'Zorro Daily Backtests')

fileSummary = open('C:\dev\godaddy\\mech\output\Zorro\Testz\ZorroResults.htm','rb')
session.storbinary('STOR /mech/output/Zorro/Testz/ZorroResults.htm', fileSummary)     # send the file
fileSummary.close()   
    
session.quit()     