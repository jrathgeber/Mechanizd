# -*- coding: utf-8 -*-

"""

Created on Saturday August 24th 2019

Working on it today on Sunday December 27th 2020

@author: Jason Rathgeber

"""

import numerox as nx
import configparser
import numerai_nomi1 as mechXg
import os
import time
import Tweet
import numeroxj as nxj
 	
from zipfile import ZipFile

def run_numerai_batch():
    
    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\etc\properties.ini') 
    
    # Numerai credentials for submission
    public = config['numerai']['public']
    secret = config['numerai']['secret']
        
    # compute the tournament numer
    # week = time.strftime("%U")
    # contest = str(int(week) + 245)
    
    # week = time.strftime("%U")
    # day = int(time.strftime("%u"))
    # contest = str(int(week) + 297)
    # if day == 7: # Sunday
    #     contest = str(int(week) + 296)

    day = int(time.strftime("%j"))  # 324
    contest = str(day + 405)
    #print(str(contest))
    #run_numerai_batch()

    print("\n Numerai Contest..." + contest)

    # Work out directory and create if not exists
    directory = 'F:\\Numerai\\numerai' + contest + '\\'

    first = "FALSE"

    if not os.path.exists(directory):
    
        first = "TRUE"
        
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


    #if not first == "TRUE" :
    if not first == "FALSE" :

        # Tweet
        print("Tweeting ..")
        # Tweet.tweetSomething('I am uploading submission for numer.ai [' + contest + '] with correlation [' + rvalue + '] ')
        # 
        
        # Tweet.tweetSomething('Cold in NY today')
    
        # Upload to numerai
        print("Uploading")
        names = ('nomi',)     
        for name in names:
            nxj.upload(directory + name + '_submission.csv', name, public, secret)
    
    print("All Done")
  

if __name__ == '__main__':
    
    day = int(time.strftime("%j"))  # 324
    contest = day + 405
    print(str(contest))
    run_numerai_batch()

