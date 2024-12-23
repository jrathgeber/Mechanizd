# -*- coding: utf-8 -*-

"""
Created on Sum Dec 22 2024

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

GPT_MODEL = 'gpt-4o-mini'
O1_MODEL = 'o1-mini'

good_prompt = ("Generate a function that outputs the SMILES IDs for all the molecules involved in insulin.")
response = client.chat.completions.create(model=O1_MODEL,messages=[{"role":"user","content": good_prompt}])

print(response)