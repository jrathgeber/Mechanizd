# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:00:11 2020

@author: Jason
"""



from google.cloud import language_v1
from google.cloud.language_v1 import enums


#def sample_classify_text(gcs_content_uri):
   
"""
   Classifying Content in text file stored in Cloud Storage

    Args:
      gcs_content_uri Google Cloud Storage URI where the file content is located.
      e.g. gs://[Your Bucket]/[Path to File]
      The text file must include at least 20 words.
"""

client = language_v1.LanguageServiceClient()

gcs_content_uri = 'gs://cloud-samples-data/language/classify-entertainment.txt'

    # Available types: PLAIN_TEXT, HTML
type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
language = "en"
document = {"gcs_content_uri": gcs_content_uri, "type": type_, "language": language}

response = client.classify_text(document)
# Loop through classified categories returned from the API
for category in response.categories:
    # Get the name of the category representing the document.
    # See the predefined taxonomy of categories:
    # https://cloud.google.com/natural-language/docs/categories
    print(u"Category name: {}".format(category.name))
    # Get the confidence. Number representing how certain the classifier
    # is that this category represents the provided text.
    print(u"Confidence: {}".format(category.confidence))


