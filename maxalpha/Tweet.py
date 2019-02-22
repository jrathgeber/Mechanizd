# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# Ty to : 

# https://www.geeksforgeeks.org/tweet-using-python/

import tweepy 
import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

   
def tweetSomething(something):

    tickerList = ['ZSAN', 'VIPS']          
      
    # personal details 
    consumer_key=config['twitter']['consumer_key']
    consumer_secret=config['twitter']['consumer_secret']
    
    access_token=config['twitter']['access_token']
    access_token_secret=config['twitter']['access_token_secret']
      
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
      
    # authentication of access token and secret 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
      
    # update the status 
    #api.update_status(status ="Penny Stock Watchlist for today : $TMSR $AMRS $CRON") 
    #api.update_status(status = something)
    api.update_status(status ='Day Trading Watchlist $' + ', $'.join(tickerList))
    
tweetSomething('Hi')