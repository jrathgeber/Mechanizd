import prompts.Trifindr1
import wordpress.WordPressUpload as wp
import ai.OpenAi013 as ai
import ai.OpenAi01 as news
import ai.Dalle as dale

import requests

def create_news_post(key_words):

    # Slugs
    slug = key_words.replace(" ", "_")
    name = slug

    # Post
    prompt = "Create a very short article list some news and events about Triathlon."
    news_post = news.write_article(key_words, prompt)

    # Image
    slug = key_words.replace(" ", "_")
    image = slug + ".jpg"
    url = dale.create_image("", "", slug, key_words, "")
    download_image(url, image)
    img = wp.add_a_wordpress_image(image, name)

    # Upload
    wp.post_upload(img, key_words, news_post, "https://trifindr.com",  "publish")


def create_blog_post(key_words):

    slug = key_words.replace(" ", "_")
    name = slug

    file_path_laptop_image = "../linkedin\\"

    prompt = content.prompts.Trifindr1.further_info

    html_content_2 = ai.write_article(key_words, prompt)

    img = wp.add_a_wordpress_image(file_path_laptop_image, name)

    wp.post_upload(img, key_words, html_content_2, "https://trifindr.com", "la", "en", "publish")


def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {file_name}")
    else:
        print("Failed to retrieve the image")


def create_product(url, title, description, price, images):

    slug = title.replace(" ", "_")

    image = slug + ".jpg"

    download_image(images[0], image)

    image = wp.add_a_wordpress_image(image, slug)

    wp.product_upload(url, slug, title, description, price, image)