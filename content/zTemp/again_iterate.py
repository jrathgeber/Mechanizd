import os

directory = "path/to/your/directory"

for filename in os.listdir(directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        print(os.path.splitext(filename)[0])