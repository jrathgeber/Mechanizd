import openai
import requests
import io
from PIL import Image


import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')


openai.api_key = config['openai']['api_key']


response = openai.Image.create(
    prompt="Market Crash",
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']

image_data = requests.get(image_url).content
image = Image.open(io.BytesIO(image_data))

image.save("market_crash.png")
print("Image saved as market_crash.png")