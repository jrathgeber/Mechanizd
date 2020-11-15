# -*- coding: utf-8 -*-

"""
Created on Fri Oct 16 13:35:16 2020

@author: Jason

"""

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u"Hello, Hackathon"
document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))