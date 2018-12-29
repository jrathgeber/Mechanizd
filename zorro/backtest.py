# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 06:52:28 2017

@author: Jason
"""

from subprocess import Popen

import ftplib
import time
from shutil import copyfile

import FileReadingBackTest as FR

import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['url']
gduser = config['godaddy']['user']
gdpass = config['godaddy']['pass']

timestr = time.strftime("%d%m%y")
session = ftplib.FTP(gdurl,gduser,gdpass)

models = ('downloadj','J12a','J12b','J12c')

fileTypes = ('.png','.htm','.txt', '_pnl.csv', '_test.log')

for model in models:

    #j12 = [r"F:\\Zorro\\Zorro_19X\\Zorro.exe", "-run", model, "-c" , "J1"]
    #j12_prog = Popen(j12)
    #stdout, stderr = j12_prog.communicate()
    
    if model != 'downloadj' :

        for fileType in fileTypes:

            copyfile('F:\Zorro\\Zorro_19X\Log\\' + model + fileType, 'C:\dev\godaddy\\mech\\output\Zorro\\Test\\' + model + '_' + timestr + fileType)
            
            file = open('F:\Zorro\\Zorro_19X\Log\\' + model + fileType,'rb')
            session.storbinary('STOR /mech/output/Zorro/Test/' + model + '_' + timestr + fileType, file)
            file.close()
    
        copyfile('F:\Zorro\\Zorro_19X\Log\\testtrades.csv', 'C:\dev\godaddy\\mech\\output\Zorro\\Test\\' + model + '_' + timestr + '_testtrades.csv')    
        
        file = open('F:\Zorro\\Zorro_19X\Log\\testtrades.csv','rb')
        session.storbinary('STOR /mech/output/Zorro/Test/' + model + '_' + timestr + '_testtrades.csv', file)
        file.close()    
    

FR.fileReading("C:\dev\godaddy\\mech\output\Zorro\\Test\\J*.htm", 'C:\dev\godaddy\\mech\output\Zorro\Test\ZorroResults.htm', 'Zorro Backtest')

fileSummary = open('C:\dev\godaddy\\mech\output\Zorro\Test\ZorroResults.htm','rb')
session.storbinary('STOR /mech/output/Zorro/Test/ZorroResults.htm', fileSummary)     # send the file
fileSummary.close()   
    
session.quit()     