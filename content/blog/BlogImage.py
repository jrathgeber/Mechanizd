import content.ai.Dalle as ai
import requests
import os
from PIL import Image


def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {file_name}")
    else:
        print("Failed to retrieve the image")


def create_thumbnail(input_path, output_path, size=(800, 450)):
    try:
        # Open the original image
        with Image.open(input_path) as img:
            # Create a thumbnail
            img.thumbnail(size)

            # Save the thumbnail
            img.save(output_path)

        print(f"Thumbnail created successfully: {output_path}")
    except Exception as e:
        print(f"Error creating thumbnail: {str(e)}")


def new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, ddate):

    image_url = ai.create_image(file_path_laptop_image, article_number, slug, key_words, ddate)

    file_name = file_path_laptop_image + article_number + '_' + slug + '.jpg'
    file_name_thumb = file_path_laptop_thumb + article_number + '_' + slug + '.jpg'

    ' Download to images and copy to thumbs'
    download_image(image_url, file_name)
    create_thumbnail(file_name, file_name_thumb)


if __name__ == "__main__":

    '''
    create_thumbnail("C:\\dev\\godaddy\\vcard\\assets\\custom\\images\\blog\\043_how_to_download_a_youtube_video_transcript_with_python.jpg",
    "C:\\dev\\godaddy\\vcard\\assets\custom\\images\\blog\\thumbs\\043_how_to_download_a_youtube_video_transcript_with_python.jpg")

    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):

    '''
    directory = "C:\\dev\\godaddy\\vcard\\assets\\custom\\images\\blog\\"

    dir_out = "C:\\dev\\godaddy\\vcard\\assets\custom\\images\\blog\\thumbs\\v2\\"



    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg')):
            file_path = os.path.join(directory, filename)
            name = os.path.splitext(filename)[0]
            print(name)
            create_thumbnail(file_path,dir_out + name + '.jpg')