import OpenDalE as ai
import requests

# HTML content you want to save

def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {file_name}")
    else:
        print("Failed to retrieve the image")


def new_image(file_path_laptop, article_number, slug, key_words, ddate):

    image_url = ai.create_image(file_path_laptop, article_number, slug, key_words, ddate)

    file_name = 'zappy\\' + article_number + '_' + slug + '.jpg'

    download_image(image_url, file_name)