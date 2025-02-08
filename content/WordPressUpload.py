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

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "status": postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
    })

    response = requests.request(
        "POST",
        WP_url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print(response)
