# -*- coding: utf-8 -*-

import sendMail
import time
import ftplib
import psutil

from subprocess import Popen
from subprocess import TimeoutExpired
from shutil import copyfile
import FileReadingRE as FR


# Used to Shut down RE after Market is closed
def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


#   Runs the following : 
#   "C:\Program Files (x86)\Yye Software\RightEdge 2010\RightEdge.exe" /W:"Nasdaq100" /P:"C:\dec\RightEdge\Systems\BarCheckerEQ\BarChecker.rep" /S /U /E
#   and send an email output

def runRightEdge(system, name, watchlist, mode, daterun, get_prices, closeup):
   
    models = ('/W:'+ watchlist + daterun,)
                  
    timestr = time.strftime("%d%m%y")
    
    #Main Model Loop Through
    for model in models:
    
        cc_list = ('jrathgeber@yahoo.com')
        
        systemrep = "/P:C:\\dec\\RightEdge\\Systems\\" + system + "\\" + name + ".rep"
        systemroot = "C:\\dec\\RightEdge\\Systems\\" + system +"\\"
        systemoutput = "C:\\dec\\RightEdge\\Systems\\" + system +"\\output.html"
        systemoutputtxt = "C:\\dec\\RightEdge\\Systems\\" + system +"\\output.txt"
    
        params = [r"C:\Program Files (x86)\Yye Software\RightEdge 2010\RightEdge.exe",  model , systemrep, mode, get_prices, closeup]
        p = Popen(params)
        #stdout, stderr = p.communicate()
        

        print (p.pid)
    
        # After 6.5 hours shut down
        try:
            p.wait(timeout=3600*10)
        except TimeoutExpired:
            print ('Kill')
            kill(p.pid)
        
    
        # Loop through each ticker
        with open(systemoutputtxt, 'r') as f:
    
            ticker_list = f.read().splitlines()
            #print (ticker_list)
    
            # Append Images to list
            image_list = []
            for i in ticker_list:
                image_list.append(systemroot + "images\\" + i + ".png")
                #print (image_list)
    
        with open(systemoutput, 'r') as f:
            data = str(f.read())
            sendMail.send_mail('jrathgeber@yahoo.com', cc_list, 'RE ' + system + ' Breakout Results', data, image_list)
    
        copyfile(systemoutput, 'C:\\dev\godaddy\\mech\\output\RightEdge\\Live\\' + model.replace('/W:','').replace('/','') + '_' + timestr + '.htm')  
    
        session = ftplib.FTP('ftp.jasonrathgeber.com','jason@jasonrathgeber.com','RcGFhn$qko2.')
        file = open(systemoutput,'rb')
        session.storbinary('STOR /mech/output/RightEdge/Live/' + model.replace('/W:','').replace('/','') + '_' + timestr + '.htm', file)     # send the file
        file.close()                                    # close file and FTP
    
    FR.fileReading("C:\dev\godaddy\\mech\output\RightEdge\\Live\\*.htm", 'C:\dev\godaddy\\mech\output\RightEdge\Live\RightEdgeResults.htm', 'RightEdge - Live Trading')
    
    fileSummary = open('C:\dev\godaddy\\mech\output\RightEdge\Live\RightEdgeResults.htm','rb')
    session.storbinary('STOR /mech/output/RightEdge/Live/RightEdgeResults.htm', fileSummary)     # send the file
    fileSummary.close()   
        
    session.quit()