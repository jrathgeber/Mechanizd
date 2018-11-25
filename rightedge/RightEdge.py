# -*- coding: utf-8 -*-

import sendMail
import time
import ftplib

from subprocess import Popen
from shutil import copyfile
import FileReadingRE as FR

import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['url']
gduser = config['godaddy']['user']
gdpass = config['godaddy']['pass']


#   Runs the following : 
#   "C:\Program Files (x86)\Yye Software\RightEdge 2010\RightEdge.exe" /W:"Nasdaq100" /P:"C:\dec\RightEdge\Systems\BarCheckerEQ\BarChecker.rep" /S /U /E
#   and send an email output

models = ('/W:Jason',)
#models = ('/W:Jason','/W:TSX','/W:Nasdaq100')
#models = ('/W:Jason','/W:TSX','/W:Nasdaq100','/W:Fonsie','/W:HF')
#models = ('/W:TSX',)

get_prices = '/U'
#get_prices = ''

cc_list_dad = 'rathgeber.webster@gmail.com'

timestr = time.strftime("%d%m%y")

#Main Model Loop Through
for model in models:

    cc_list = ('jrathgeber@yahoo.com')
    if "TSX" in model: 
    # cc_list = ('jrathgeber@yahoo.com')
      cc_list = ('jrathgeber@yahoo.com','rathgeber.webster@gmail.com')

    params = [r"C:\Program Files (x86)\Yye Software\RightEdge 2010\RightEdge.exe",  model , '/P:C:\dec\RightEdge\Systems\SymbolRanking\SymbolRanking.rep', '/S', get_prices, '/E']
    p = Popen(params)
    stdout, stderr = p.communicate()

    # Loop through each ticker
    with open('C:\dec\RightEdge\Systems\SymbolRanking\output.txt', 'r') as f:

        ticker_list = f.read().splitlines()
        #print (ticker_list)

        # Append Images to list
        image_list = []
        for i in ticker_list:
            image_list.append("C:\dec\RightEdge\Systems\SymbolRanking\images\\" + i + ".png")
            #print (image_list)

    with open('C:\dec\RightEdge\Systems\SymbolRanking\output.html', 'r') as f:
        data = str(f.read())
        #sendMail.send_mail('jrathgeber@yahoo.com', cc_list, 'RE ' + model.replace('/W:','') + ' Breakout Results', data, image_list)

    copyfile('C:\dec\RightEdge\Systems\SymbolRanking\output.html', 'C:\dev\godaddy\\mech\output\RightEdge\\Hist\\' + model.replace('/W:','') + '_' + timestr + '.htm')  

    session = ftplib.FTP(gdurl,gduser,gdpass)
    file = open('C:\dec\RightEdge\Systems\SymbolRanking\output.html','rb')
    session.storbinary('STOR /mech/output/RightEdge/Hist/' + model.replace('/W:','') + '_' + timestr + '.htm', file)     # send the file
    file.close()                                    # close file and FTP

FR.fileReading("C:\dev\godaddy\\mech\output\RightEdge\\Hist\\*.htm", 'C:\dev\godaddy\\mech\output\RightEdge\Hist\RightEdgeResults.htm', 'RightEdge - Backtest YTD')

fileSummary = open('C:\dev\godaddy\\mech\output\RightEdge\Hist\RightEdgeResults.htm','rb')
session.storbinary('STOR /mech/output/RightEdge/Hist/RightEdgeResults.htm', fileSummary)     # send the file
fileSummary.close()   
    
session.quit()