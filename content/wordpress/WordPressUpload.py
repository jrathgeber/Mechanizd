# https://www.freecodecamp.org/news/how-to-generate-wordpress-posts-automatically/

import requests
import json
import configparser
from requests.auth import HTTPBasicAuth


# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

wp_user = config['wordpress']['user']
wp_pass = config['wordpress']['pass']

print("Wordpress data set...")


def post_creator(img, key_words, source, wpBaseURL, sourceLang, targetLang, postStatus):

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
       # "featured_media": img

    })

    response = requests.request(
        "POST",
        WP_url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print(response)


def add_a_wordpress_image(file_name, slug):
    """ Takes an image name, posts to WP, returns image url. """

    auth = HTTPBasicAuth(wp_user, wp_pass)
    url = "https://trifindr.com/wp-json/wp/v2/media"

    #file_name = file_path_laptop_image + '_' + slug + '.jpg'

    img_name = slug

    # Define the image
    media = {
        "file": open(file_name, "rb"),
        "caption": img_name,
        "description": img_name
    }

    # Post the image to WP
    response = requests.post(url, auth=auth, files=media)  # ! files=, not json= !


    # Check Response
    if response.status_code == 201:
        image_data = response.json()
        image_id = image_data["id"]
        image_url = image_data["source_url"]
        print(f"Image uploaded successfully! ID: {image_id}, URL: {image_url}")
    else:
        print("Error uploading image:", response.text)

    # Extract and return the image URL from returned data
    return str(json.loads(response.content)["id"])


def product_upload(url, slug, title, description, price, image_id):

    url = "https://trifindr.com/"


    # Product data
    payload = json.dumps({
        "name": title,
        "content": description,
        "status": "publish",
        "type": "external",
        "regular_price": price,
        "images": [{"id": image_id}],
        "external_url": url,
        "slug": slug,
        "button_text" : "Buy On Amazon",
        "short_description" : description
    })

    # Authentication
    auth = HTTPBasicAuth(wp_user, wp_pass)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # API endpoint
    endpoint = f"{url}/wp-json/wc/v2/products"

    # Send the request
    response = requests.request(
        "POST",
        endpoint,
        data=payload,
        headers=headers,
        auth=auth
    )

    # Check the response
    if response.status_code == 201:
        print("Product created successfully!")
        print(response.json())
    else:
        print(f"Error creating product: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    product_upload()
    #add_a_wordpress_image("https://m.media-amazon.com/images/I/81FB3Yd2sTL._AC_SL1500_.jpg", "bike")