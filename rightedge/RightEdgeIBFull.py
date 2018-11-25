# -*- coding: utf-8 -*-

import sendMail
import time
import ftplib

from subprocess import Popen
from shutil import copyfile
import FileReadingRE as FR

# Runs the following : 

daterun = time.strftime("%Y%m%d")

#models = ('/W:Jason',)
#models = ('/W:Jason','/W:TSX','/W:Nasdaq100')
#models = ('/W:Jason','/W:TSX','/W:Nasdaq100','/W:Fonsie','/W:HF')
models = ('MaxAlphaStopAndReverse', 'MaxAlphaShortOnly', 'MaxAlphaShortOnlyV2', 'MaxAlphaMinShort')

get_prices_XX = '/U'
get_prices = ''

timestr = time.strftime("%d%m%y")

#Main Model Loop Through
for model in models:

    cc_list = ('jrathgeber@yahoo.com')
    if "TSX" in model: 

       cc_list = ('jrathgeber@yahoo.com')

    params = [r"C:\Program Files (x86)\Yye Software\RightEdge 2010\RightEdge.exe",  '/W:MaxAlpha' , "/P:C:\dec\RightEdge\Systems\\" + model + "\MaxAlpha.rep", '/S', get_prices, '/E']
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
        sendMail.send_mail('jrathgeber@yahoo.com', cc_list, 'RE ' + model + ' Breakout Results', data, image_list)

    copyfile("C:\dec\RightEdge\Systems\\" + model + "\output.html", 'C:\dev\godaddy\\mech\output\RightEdge\\Hist\\' + model + '_' + timestr + '.htm')  

    session = ftplib.FTP('ftp.jasonrathgeber.com','jason@jasonrathgeber.com','RcGFhn$qko2.')
    file = open("C:\dec\RightEdge\Systems\\" + model + "\output.html",'rb')
    session.storbinary('STOR /mech/output/RightEdge/Hist/' + model + '_' + timestr + '.htm', file)     # send the file
    file.close()                                    # close file and FTP

FR.fileReading("C:\dev\godaddy\\mech\output\RightEdge\\Hist\\*.htm", 'C:\dev\godaddy\\mech\output\RightEdge\Hist\RightEdgeResults.htm', 'Rightedge Backtest - YTD IB')

fileSummary = open('C:\dev\godaddy\\mech\output\RightEdge\Hist\RightEdgeResults.htm','rb')
session.storbinary('STOR /mech/output/RightEdge/Hist/RightEdgeResults.htm', fileSummary)     # send the file
fileSummary.close()   
    
session.quit()