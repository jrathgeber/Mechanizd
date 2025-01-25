# -*- coding: utf-8 -*-

"""
Created on Sum Jan 22 2025
@author: Jason R
"""

import openai
from openai import OpenAI
import configparser


def create_image(file_path_laptop, article_number, slug, key_words, todaydate):

    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    client = OpenAI(
        # This is the default and can be omitted
        api_key=config['openai']['api_key'],
    )

    response = client.images.generate(
        model="dall-e-3",
        prompt=key_words,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    print(response.data[0].url)

    return response.data[0].url