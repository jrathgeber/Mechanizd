# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 06:52:28 2017

@author: Jason
"""

import sendMail;
import os;

os.chdir('c:\\dep\\rightedge\\')

#cc_list = ('jrathgeber@yahoo.com','rathgeber.webster@gmail.com')
cc_list = ('jrathgeber@yahoo.com')   

#send live MaxAlpha Output
with open('C:\dec\RightEdge\Systems\MaxAlphaOne\output.html', 'r') as f:
    data = str(f.read())
    sendMail.send_mail('jrathgeber@yahoo.com', cc_list, 'Max Alpha MA1 Live', data, ['C:\dec\RightEdge\Systems\MaxAlphaOne\output.txt'])
    
# Send Back Test    
exec(open('C:\\dep\\rightedge\\RightEdgeIB.py').read())
    
# Send Z7 Live Status    
with open('F:\Zorro\Zorro_19X\Log\Z7.htm', 'r') as f:
    data = str(f.read())
    sendMail.send_mail('jrathgeber@yahoo.com', 'jrathgeber@yahoo.com', 'Zorro Summary Z7', data, ['F:\Zorro\Zorro\Log\Z7.txt'])    
    
# Backtest Js and download prices    
exec(open('C:\\dep\\zorro\\backtest.py').read())