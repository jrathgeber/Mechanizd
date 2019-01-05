# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:34:22 2017

@author: Jason
"""

import ftplib
import time
import urllib.request

import os;
os.chdir('C:\\dep\\Mechanizd\\batch\\')

import FileReading as FR
from shutil import copyfile
import configparser

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['url']
gduser = config['godaddy']['user']
gdpass = config['godaddy']['pass']


#timestr = time.strftime("%Y%m%d_%H%M%S")
timestr = time.strftime("%d%m%y")

models = ('Z1','Z2','Z12')
#models = ('Z1',)


session = ftplib.FTP('ftp.jasonrathgeber.com',gduser,gdpass)

#Main Model Loop Through
for model in models:
    ver = model.replace("Z", "").replace("12", "3")
    name = 'http://52.186.84.170/' + model + '.htm'
    print(name)
    urllib.request.urlretrieve(name, 'C:\dev\godaddy\\mech\output\Zorro\\Mech1\\' + model + '_' + timestr + '.htm')
    file = open('C:\dev\godaddy\\mech\output\Zorro\\Mech1\\' + model + '_' + timestr + '.htm','rb')
    session.storbinary('STOR /mech/output/Zorro/Mech1/' + model + '_' + timestr + '.htm', file)
    file.close()
    
    name2 = 'http://52.186.84.170/' + model + '.png'
    urllib.request.urlretrieve(name2, 'C:\dev\godaddy\\mech\output\Zorro\\Mech1\\' + model + '.png')
    file2 = open('C:\dev\godaddy\\mech\output\Zorro\\Mech1\\' + model + '.png','rb')
    session.storbinary('STOR /mech/output/Zorro/Mech1/' + model + '.png', file2)
    file2.close()        
       
FR.fileReading("C:\dev\godaddy\\mech\output\Zorro\\Mech1\\Z*.htm", 'C:\dev\godaddy\\mech\output\Zorro\Mech1\ZorroResults.htm', '<a href="http://52.186.84.170">Zorro Mech1</a>')

fileSummary = open('C:\dev\godaddy\\mech\output\Zorro\Mech1\ZorroResults.htm','rb')
session.storbinary('STOR /mech/output/Zorro/Mech1/ZorroResults.htm', fileSummary)     # send the file
fileSummary.close()   

with open('C:\dev\godaddy\\mech\output\Zorro\Mech1\ZorroResults.htm', 'r') as f:
    data = str(f.read())
    #sendMail.send_mail('jrathgeber@yahoo.com', 'jrathgeber@yahoo.com', 'Zorro Summary', data, '')
    
session.quit()

