import OpenDalE as ai
import requests
from shutil import copyfile

# HTML content you want to save

def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {file_name}")
    else:
        print("Failed to retrieve the image")


def new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, ddate):

    image_url = ai.create_image(file_path_laptop_image, article_number, slug, key_words, ddate)

    file_name = file_path_laptop_image + article_number + '_' + slug + '.jpg'
    file_name_thumb = file_path_laptop_thumb  + article_number + '_' + slug + '.jpg'

    ' Download to images and copy to thumbs'
    download_image(image_url, file_name)
    copyfile(file_name, file_name_thumb)