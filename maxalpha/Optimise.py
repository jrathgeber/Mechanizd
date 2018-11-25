# -*- coding: utf-8 -*-

import RightEdge as RE;


def optimise(system):

    daterun = ''
    getprices = ''
    closeup = ''
    
    mode = '/O:C:\dep\maxalpha\zParams_20180227.txt'
    
    opy = open("C:\dep\maxalpha\zParams_20180227.txt", "w")
    
    #opy.write("ADXPeriods, 1000,2000,1000\n")
    opy.write("BreakOutBuyDays,50,500,10\n")
    opy.write("BreakOutSellDays,50,500,10\n")
    #opy.write("BeakOutBuyHeight,100,500,100\n")
    #opy.write("COG,25,500,25\n")
    #opy.write("MA1,25,500,25\n")
    #opy.write("MA2,5,100,5\n")
    #opy.write("RSIPeriods,25,500,25\n")
    #opy.write("StopLoss,.1,2,10\n")
    #opy.write("TakeProfit,.1,2,10\n")
    
    opy.close()
    
    RE.runRightEdge(system, 'MaxAlpha', mode, daterun, getprices, closeup);