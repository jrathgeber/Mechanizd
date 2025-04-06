from shutil import copyfile

source_file = 'C:\\dep\\Mechanizd\\content\\zTemp\\SEOWriting\\Cannondale synapse 105.html'
destination_file = 'C:\\\dev\\godaddy\\vcard\\blogpost\\articles\\article_001_cannondale.html'

try:
    copyfile(source_file, destination_file)
    print(f"File copied successfully from {source_file} to {destination_file}")
except FileNotFoundError:
    print(f"Source file {source_file} not found.")
except PermissionError:
    print("Permission denied. Unable to copy file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
