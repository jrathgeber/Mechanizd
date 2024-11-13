import configparser

from medium_api import Medium

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

# Numerai credentials for submission
api_key = config['medium']['token']


# Create a `Medium` Object
medium = Medium(api_key)

# Get the "Article" object and print markdown
article = medium.article(article_id="https://medium.com/@jasonrathgeber/2024-election-and-fintech-89482f8d9c5e")

print(article.markdown)