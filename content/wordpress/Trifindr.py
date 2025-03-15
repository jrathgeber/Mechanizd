import content.prompts.Trifindr1
import content.wordpress.WordPressUpload as wp
import content.ai.OpenAi013 as ai
import requests

def create_blog_post(key_words):

    slug = key_words.replace(" ", "_")
    name = slug

    file_path_laptop_image = "../temp\\"

    prompt = content.prompts.Trifindr1.further_info

    html_content_2 = ai.write_article(key_words, prompt)

    img = wp.add_a_wordpress_image(file_path_laptop_image, name)

    wp.post_creator(img, key_words, html_content_2, "https://trifindr.com", "la", "en", "publish")


def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {file_name}")
    else:
        print("Failed to retrieve the image")


def create_product(title, description, price, image):

    #download_image("https://m.media-amazon.com/images/I/81FB3Yd2sTL._AC_SL1500_.jpg", "bike_image.jpg")

    image = wp.add_a_wordpress_image("bike_image.jpg", "bike_image")

    file_path_laptop_image = "../temp\\"

    wp.product_upload(title, description, price, image)