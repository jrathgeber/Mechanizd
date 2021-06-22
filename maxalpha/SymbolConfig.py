# -*- coding: utf-8 -*-

import time
from shutil import copyfile

def symbolwrite(copy, todaydate, symbols, maxdata):

    for symbol in symbols:  
        copy.write('                 <WatchListItem>\n')
        copy.write('                  <IsFolder>false</IsFolder>\n')
        copy.write('                  <BarConstruction>Default</BarConstruction>\n')
        copy.write('                  <Symbol>\n')
        copy.write('                   <StrikePrice>0</StrikePrice>\n')
        copy.write('                   <ExpirationDate>0001-01-01T00:00:00</ExpirationDate>\n')
        copy.write('                   <Name>' + symbol + '</Name>\n')
        copy.write('                   <SymbolInformation>\n')
        copy.write('                    <Margin>0</Margin>\n')
        copy.write('                    <TickSize>0</TickSize>\n')
        copy.write('                    <ContractSize>0</ContractSize>\n')
        copy.write('                    <DecimalPlaces>2</DecimalPlaces>\n')
        copy.write('                    <ShortMargin>0</ShortMargin>\n')
        copy.write('                    <CustomHistoricalData>' + todaydate + '</CustomHistoricalData>\n')
        copy.write('                    <CustomLiveData>' + maxdata + '</CustomLiveData>\n')
        copy.write('                    </SymbolInformation>\n')
        copy.write('                   </Symbol>\n')
        copy.write('                  </WatchListItem>\n')

def copywrite(copy, todaydate, symbols, maxdata):
      
        copy.write('             <WatchListItem>\n')
        copy.write('               <IsFolder>true</IsFolder>\n')
        copy.write('               <BarConstruction>Default</BarConstruction>\n')
        copy.write('               <Folder>\n')
        copy.write('                <FolderName>' + todaydate +'</FolderName>\n')
        copy.write('                <Contents>\n')
        symbolwrite(copy, todaydate, symbols, maxdata)
        copy.write('                 </Contents>\n')
        copy.write('                 <Frequency>-1</Frequency>\n')
        copy.write('                 <InheritsHistService>true</InheritsHistService>\n')
        copy.write('                 <HistService />\n')
        copy.write('                 <InheritsRealtimeService>true</InheritsRealtimeService>\n')
        copy.write('                 <RealtimeService />\n')
        copy.write('                 <InheritsBrokerService>true</InheritsBrokerService>\n')
        copy.write('                 <BrokerService />\n')
        copy.write('                 <InheritsSaveTicks>true</InheritsSaveTicks>\n')
        copy.write('                 <SaveTicks>false</SaveTicks>\n')
        copy.write('                 <InheritsSaveBars>true</InheritsSaveBars>\n')
        copy.write('                 <SaveBars>true</SaveBars>\n')
        copy.write('                 <DownloadStartDate>0001-01-01T00:00:00</DownloadStartDate>\n')
        copy.write('                 <InheritsDownloadStartDate>true</InheritsDownloadStartDate>\n')
        copy.write('                 <InheritsFrequency>true</InheritsFrequency>\n')
        copy.write('               </Folder>\n')
        copy.write('             </WatchListItem>\n')


def getSymbolConfig(tickers, todaydate, maxdata):

    #tickers = ['SPI', 'ICON', 'CNET', 'RIOT', 'HMNY']
    #todaydate = "20180127"
    
    f = open(r"C:\Users\Jason\AppData\Roaming\Yye Software\RightEdge\2010.1.0.0\SymbolConfig.xml", "r")
    #f = open(r"SymbolConfigStart.xml", "r")
    
    copy = open("SymbolConfig.xml", "w")
    
    x=0
    for line in f:
        x=x*2
        if x==4:
            copywrite(copy, todaydate, tickers, maxdata)
        if 'MaxAlpha' in line:
            x=1     
        copy.write(line)
        
        
        
    # print(line)
    f.close()
    copy.close()
    
    # Give it some time
    time.sleep(3)
    
    # Put the file in the right place
    copyfile('SymbolConfig.xml', 'C:\\Users\\Jason\\AppData\\Roaming\\Yye Software\\RightEdge\\2010.1.0.0\\SymbolConfig.xml') 
    
    #Backup
    copyfile('C:\\Users\\Jason\\AppData\\Roaming\\Yye Software\\RightEdge\\2010.1.0.0\\SymbolConfig.xml', 'F:\\RightEdge\\MaxAlpha\\SymbolConfig'+todaydate+'.xml') 