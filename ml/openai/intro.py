# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:24:03 2023

@author: Jason
"""

import os
import openai

import configparser


# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 
    
# Numerai credentials for submission
openai.api_key = config['numerai']['secret']

openai.organization = "org-aoyNnQ1dPcIRRhnCVU3Lcc95"
openai.api_key = config['openai']['api_key']
openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)