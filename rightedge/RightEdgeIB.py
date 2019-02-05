# -*- coding: utf-8 -*-

import sendMail
import time
import ftplib

from subprocess import Popen
from shutil import copyfile

import os;
os.chdir('C:\\dep\\Mechanizd\\batch\\')

import FileReadingRE as FR

import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['godaddy.url']
gduser = config['godaddy']['godaddy.user']
gdpass = config['godaddy']['godaddy.pass']

url = config['yahoo']['yahoo.url']
user = config['yahoo']['yahoo.user']
password = config['yahoo']['yahoo.pass']
server = config['yahoo']['yahoo.server']
port = config['yahoo']['yahoo.port']
username = config['yahoo']['yahoo.username']

# Runs the following : 
# "C:\Program Files (x86)\Yye Software\RightEdge 2010\RightEdge.exe" /W:"Nasdaq100" /P:"C:\dec\RightEdge\Systems\BarCheckerEQ\BarChecker.rep" /S /U /E
# and send an email output

daterun = time.strftime("%Y%m%d")
#daterun = '20181026'

#models = ('/W:Jason',)
#models = ('/W:Jason','/W:TSX','/W:Nasdaq100')
#models = ('/W:Jason','/W:TSX','/W:Nasdaq100','/W:Fonsie','/W:HF')
models = ('MaxAlphaStopAndReverse', 'MaxAlphaShortOnly', 'MaxAlphaMinShort', 'MaxAlphaOne', 'MaxAlpha25cent')

get_prices_XX = '/U'
get_prices = ''

timestr = time.strftime("%d%m%y")

#Main Model Loop Through
for model in models:

    cc_list = (yuser)
    if "TSX" in model: 

       cc_list = (yuser)
#      cc_list = ('jrathgeber@yahoo.com','rathgeber.webster@gmail.com')

    params = [r"C:\Program Files (x86)\Yye Software\RightEdge 2010\RightEdge.exe",  '/W:MaxAlpha' + '/'+ daterun , "/P:C:\dec\RightEdge\Systems\\" + model + "\MaxAlpha.rep", '/S', get_prices, '/E']
    p = Popen(params)
    stdout, stderr = p.communicate()

    # Loop through each ticker
    with open("C:\dec\RightEdge\Systems\\" + model + "\output.txt", 'r') as f:

        ticker_list = f.read().splitlines()
        #print (ticker_list)

        # Append Images to list
        image_list = []
        for i in ticker_list:
            image_list.append("C:\dec\RightEdge\Systems\\" + model + "\images\\" + i + ".png")
            #print (image_list)

    with open("C:\dec\RightEdge\Systems\\" + model + "\output.html", 'r') as f:
        data = str(f.read())
        sendMail.send_mail('jrathgeber@yahoo.com', cc_list, 'RE ' + model.replace('/W:','') + ' Breakout Results', data, image_list, server, port, username, password)

    copyfile("C:\dec\RightEdge\Systems\\" + model + "\output.html", 'C:\dev\godaddy\\mech\output\RightEdge\\Close\\' + model.replace('/W:','') + '_' + timestr + '.htm')  

    session = ftplib.FTP(gdurl,gduser,gdpass)
    file = open("C:\dec\RightEdge\Systems\\" + model + "\output.html",'rb')
    session.storbinary('STOR /mech/output/RightEdge/Close/' + model.replace('/W:','') + '_' + timestr + '.htm', file)     # send the file
    file.close()

FR.fileReading("C:\dev\godaddy\\mech\output\RightEdge\\Close\\*.htm", 'C:\dev\godaddy\\mech\output\RightEdge\Close\RightEdgeResults.htm', 'Rightedge Backtest - Today')

fileSummary = open('C:\dev\godaddy\\mech\output\RightEdge\Close\RightEdgeResults.htm','rb')
session.storbinary('STOR /mech/output/RightEdge/Close/RightEdgeResults.htm', fileSummary)     # send the file
fileSummary.close()   
    
session.quit()