# Path to your image file (can be an image that exists on your computer)
image_path = 'image.jpeg'

# Path to save the image to (output path)
output_path = 'saved_image.jpeg'

# Open and save the image to a new location
with open(image_path, 'rb') as img_file:
    image_data = img_file.read()

# Save the image data to a new file
with open(output_path, 'wb') as out_file:
    out_file.write(image_data)

print(f"Image has been saved as {output_path}")
