# -*- coding: utf-8 -*-

#import pandas as pd
import traceback
#import fix_yahoo_finance as yf
import quandl
#import iexfinance as iex
#import #nsepy
import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

   
# personal details 
quandl_key=config['quandl']['quandl.apikey']


from quandl.errors.quandl_error import AuthenticationError

def get_quantinsti_api_key():
    """
        This function returns the Quandl's API key which is used to access quandl data
        To get your API key, sign up for a free Quandl account
        Then, you can find your API key on Quandl account settings page
    """
    return quandl_key

def get_data(ticker, start_date='2016-01-01', end_date='2017-01-01'):
    """
        This function fetches the data from different web source such as Quandl, Yahoo finance and NSEPy
    """
    try:
        df = quandl.get('WIKI/'+ticker, start_date=start_date, end_date=end_date, api_key=get_quantinsti_api_key())
        df['Source'] = 'Quandl Wiki'
        return df[['Open','High','Low','Close','Volume','Source']]
    except AuthenticationError as a:        
        print(a)        
        print("Please replace the line no. 13 in quantrautil.py file with your Quandl API Key")
    except:
        print(traceback.print_exc())