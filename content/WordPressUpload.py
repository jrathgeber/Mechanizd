import requests
import base64
import json

import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')


username = config['wordpress']['user']
password = config['wordpress']['pass']

creds = username + ':' + password

print(creds)

cred_token = base64.b64encode(creds.encode())

print(cred_token)

header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}

print(header)

url = "https://trifindr.com/wp-json/wp/v2"

post = {
 'title' : 'This is WordPress Python Integration',

 'content' : 'Hello, this content is published using WordPress Python Integration',
 'status' : 'publish',
 'categories': 5,
 'date' : '2025-02-5T11:00:00'
}

blog = requests.post(url + '/posts' , headers=header , json=post)
print(blog)