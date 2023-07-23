# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# Ty to : 

# https://www.geeksforgeeks.org/tweet-using-python/

import tweepy 
import configparser
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

   
def tweetSomething(something):

    # personal details
    consumer_key=config['twitter']['consumer_key']
    consumer_secret=config['twitter']['consumer_secret']
    access_token=config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']
    bearer_token = config['twitter']['bearer_token']


    client = tweepy.Client(bearer_token=bearer_token,
                            consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret)

    # Replace the text with whatever you want to Tweet about
    response = client.create_tweet(text=something)

    print(response)
    
#tweetSomething('Hi')