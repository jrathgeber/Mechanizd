# -*- coding: utf-8 -*-

"""
Created on Sum Jan 22 2025
@author: Jason R
"""

import openai
from openai import OpenAI
import configparser


def write_article(key_words, further_info):

    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    client = OpenAI(
        # This is the default and can be omitted
        api_key=config['openai']['api_key'],
    )

    GPT_MODEL = 'gpt-4o-mini'
    O1_MODEL = 'o1-mini'

    prepend = "Answer should be embedded in html tags and that's it. Nothing else."
    instructions = "Write a short blog post titled :  "
    keywords = key_words
    further_info = further_info

    # prompt = prepend + " " + instructions + " " + keywords + " " + further_info
    prompt = prepend + " " + further_info
    response = client.chat.completions.create(model=O1_MODEL,messages=[{"role":"user","content": prompt}])

    print(response.choices[0].message.content)

    return response.choices[0].message.content
