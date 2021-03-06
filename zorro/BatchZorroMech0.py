# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:34:22 2017
@author: Jason
"""

import ftplib
import time
from shutil import copyfile

import os;
os.chdir('C:\\dep\\Mechanizd\\batch\\')

import FileReading as FR
import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['godaddy.url']
gduser = config['godaddy']['godaddy.user']
gdpass = config['godaddy']['godaddy.pass']

#timestr = time.strftime("%Y%m%d_%H%M%S")
timestr = time.strftime("%d%m%y")
session = ftplib.FTP(gdurl,gduser,gdpass)


models = ('Z2',)
for model in models:
    copyfile('F:\Zorro\\Zorro\Log\\' + model + '.htm', 'C:\dev\godaddy\\mech\\output\Zorro\\Mech0\\' + model + '_' + timestr + '.htm')
    file = open('F:\Zorro\\Zorro\Log\\' + model + '.htm','rb')
    session.storbinary('STOR /mech/output/Zorro/Mech0/' + model + '_' + timestr + '.htm', file)
    file.close()

    copyfile('F:\Zorro\\Zorro\Log\\' + model + '.png', 'C:\dev\godaddy\\mech\\output\Zorro\\Mech0\\' + model + '.png')
    file2 = open('F:\Zorro\\Zorro\Log\\' + model + '.png','rb')
    session.storbinary('STOR /mech/output/Zorro/Mech0/' + model + '.png', file2)
    file2.close()        


models2 = ('Z7',)
for model in models2:
    copyfile('F:\Zorro\\Zorro_19X\Log\\' + model + '.htm', 'C:\dev\godaddy\\mech\\output\Zorro\\Mech0\\' + model + '_' + timestr + '.htm')
    file = open('F:\Zorro\\Zorro_19X\Log\\' + model + '.htm','rb')
    session.storbinary('STOR /mech/output/Zorro/Mech0/' + model + '_' + timestr + '.htm', file)
    file.close() 

    copyfile('F:\Zorro\\Zorro\Log\\' + model + '.png', 'C:\dev\godaddy\\mech\\output\Zorro\\Mech0\\' + model + '.png')
    file2 = open('F:\Zorro\\Zorro_19X\Log\\' + model + '.png','rb')
    session.storbinary('STOR /mech/output/Zorro/Mech0/' + model + '.png', file2)
    file2.close()        

FR.fileReading("C:\dev\godaddy\\mech\output\Zorro\\Mech0\\Z*.htm", 'C:\dev\godaddy\\mech\output\Zorro\Mech0\ZorroResults.htm', 'Zorro Mech0')

fileSummary = open('C:\dev\godaddy\\mech\output\Zorro\Mech0\ZorroResults.htm','rb')
session.storbinary('STOR /mech/output/Zorro/Mech0/ZorroResults.htm', fileSummary)     # send the file
fileSummary.close()   
    
session.quit()     

