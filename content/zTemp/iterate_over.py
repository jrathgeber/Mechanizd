import os
from PIL import Image

def create_thumbnail(image_path):
    with Image.open(image_path) as img:
        img.thumbnail((128, 128))
        thumbnail_path = os.path.splitext(image_path)[0] + "_thumbnail.jpg"
        img.save(thumbnail_path, "JPEG")

directory = "path/to/your/image/directory"

for filename in os.listdir(directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        file_path = os.path.join(directory, filename)
        create_thumbnail(file_path)