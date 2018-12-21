# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 10:06:53 2017

@author: Jason
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from ibapi.common import *
from ibapi.contract import *

class TestApp(EWrapper,EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def error (self, reqId:TickerId, errorCode:int, errorString:str):   
        print("Error: ", reqId, " ", errorCode, " ", errorString)
        

    def contractDetails(self,reqId:int, contractDetails:ContractDetails):        
        print("contractDeatils:", reqId, "", contractDetails)
        
def main():
    app  = TestApp()

    app.connect("127.0.0.1",4001,0)


    contract = Contract()
    
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"
    
    app.reqContractDetails(10,contract)
    
    app.run()
    
if __name__ == "__main__":
    main()
    