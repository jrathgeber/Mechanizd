# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:24:03 2023

@author: Jason
"""

import openai

import configparser


# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 
    
openai.organization = config['openai']['api_org']
openai.api_key = config['openai']['api_key']
openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": "Write me a really short inspirational tweet."}
  ]
)

print(completion.choices[0].message.content)