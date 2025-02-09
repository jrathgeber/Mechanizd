# https://www.freecodecamp.org/news/how-to-generate-wordpress-posts-automatically/

import requests
import json
import random

from requests.auth import HTTPBasicAuth
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

wp_user = config['wordpress']['user']
wp_pass = config['wordpress']['pass']

print("Wordpress data set...")


def post_creator(key_words, source, wpBaseURL, sourceLang, targetLang, postStatus):

    title_translation_text = key_words
    content_translation_text = source

    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(wp_user, wp_pass)

    image_list = ["1689", "1594", "1612"]

    random_image_list = random.choice(image_list)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "status": postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
        "featured_media": random_image_list

    })

    response = requests.request(
        "POST",
        WP_url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print(response)


import requests
import json


def add_a_wordpress_image(img_name):
    """ Takes an image name, posts to WP, returns image url. """

    auth = HTTPBasicAuth(wp_user, wp_pass)
    url = "https://trifindr.com/wp-json/wp/v2/media"

    # Define the image
    media = {
        "file": open(f"C:\\Users\\jrath\\Downloads\\triathlon-2175845_1280.jpg", "rb"),
        "caption": img_name,
        "description": img_name
    }

    # Post the image to WP
    image = requests.post(url, auth=auth, files=media)  # ! files=, not json= !

    # Extract and return the image URL from returned data
    return str(json.loads(image.content)["source_url"])
