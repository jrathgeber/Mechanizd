from openai import OpenAI
import requests


import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

api_key = config['openai']['api_key']

user_prompt =  prompt = "image of market crash"

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)

response = client.images.generate(prompt=prompt)

# Extract the URL of the generated image
image_url = response.data[0].url
image_response = requests.get(image_url)

# Save the image to a file
if image_response.status_code == 200:
    with open('generated_image.png', 'wb') as f:
        f.write(image_response.content)
    print("Image downloaded and saved as 'generated_image.png'")
else:
    print("Failed to download the image")