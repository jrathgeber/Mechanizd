# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:24:03 2023

@author: Jason
"""

import openai
from openai import OpenAI

import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

client = OpenAI(
    # This is the default and can be omitted
    api_key=config['openai']['api_key'],
)

completion = client.chat.completions.create(
 # model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Write me a really short inspirational tweet kind of like this."}
  ],
model = "gpt-3.5-turbo",
)

print(completion.choices[0].message.content)