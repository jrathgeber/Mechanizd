# -*- coding: utf-8 -*-

"""

Created on Saturday August 24th 2019

@author: Jason Rathgeber

"""

import numerox as nx
import configparser
import numerai_kg1 as mechXg
import os
import time
import Tweet
 	
from zipfile import ZipFile

def run_numerai_batch():
    
    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\etc\properties.ini') 
    
    # Numerai credentials for submission
    public = config['numerai']['public']
    secret = config['numerai']['secret']
        
    # compute the tournament numer
    week = time.strftime("%U")
    contest = str(int(week) + 192)

    # Work out directory and create if not exists
    directory = 'F:\\Numerai\\numerai' + contest + '\\'

    if not os.path.exists(directory):
        
        # Make new Dir
        os.makedirs(directory)

        # download dataset from numerai, save it and then load it
        nx.download(directory + 'numerai_dataset.zip')

        # Unzip it
        with ZipFile(directory + 'numerai_dataset.zip', 'r') as zipObj:
            
            #Extract all the contents of zip file in current directory
            zipObj.extractall(directory)

    # Run my xg boost algo on it
    rvalue = str(mechXg.main(contest))
    #rvalue = str(0.041)

    # Tweet
    print("Tweeting ..")
    Tweet.tweetSomething('Uploading my numer.ai machine learning stock market submission for round [' + contest + '] kazutsugi with correlation [' + rvalue + '] ')

    # Upload to numerai
    print("Uploading...")
    names = ('kazutsugi',)     
    for name in names:
        nx.upload(directory + name + '_new_submission.csv', name, public, secret)
    
    print("All Done")
  

if __name__ == '__main__':
    
    week = time.strftime("%U")
    contest = int(week) + 192
    print(str(contest))
    run_numerai_batch()

