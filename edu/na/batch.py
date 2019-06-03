# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:12:26 2019

@author: Jason

"""

#!/usr/bin/env python

import numerox as nx

import configparser

import numerai_xg6 as mechXg

import os
 	
from zipfile import ZipFile

def numerox_example():
    
    config = configparser.ConfigParser()
    config.read('C:\etc\properties.ini') 
    
    public = config['numerai']['public']
    secret = config['numerai']['secret']
    
    
    """
    Example of how to prepare a submission for the Numerai tournament.
    It uses Numerox which you can install with: pip install numerox
    For more information see: https://github.com/kwgoodman/numerox
    """
    
    contest = str(162)

    directory = 'F:\\Numerai\\numerai' + contest + '\\'

    if not os.path.exists(directory):
        os.makedirs(directory)

        # download dataset from numerai, save it and then load it
        # data = nx.download(directory + 'numerai_dataset.zip')
        nx.download(directory + 'numerai_dataset.zip')

        with ZipFile(directory + 'numerai_dataset.zip', 'r') as zipObj:
            #Extract all the contents of zip file in current directory
            zipObj.extractall(directory)

    # we will use logistic regression; you will want to write your own model
    # model = nx.logistic()

    # fit model with train data and make predictions for tournament data
    #prediction = nx.production(model, data, tournament='bernie')

    # save predictions to csv file
    # prediction.to_csv('logistic.csv', verbose=True)

    mechXg.main(contest)

    # upload predictions to Numerai to enter the tournament
    # create the public_id and secret_key on the Numerai website
    #
    # nx.upload('logistic.csv', tournament='bernie', public_id, secret_key)

    names = ('bernie', 'ken', 'charles', 'frank', 'hillary') 
    #names = ('hillary',)     
    
    for name in names:

        nx.upload(directory + name + '_new_submission.csv', name, public, secret)
    

if __name__ == '__main__':
    numerox_example()