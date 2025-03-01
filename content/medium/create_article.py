# https://hackernoon.com/automate-your-writing-publishing-to-medium-with-python-and-the-medium-api

import requests
import json

# Replace with your actual Medium integration token and user ID
MEDIUM_TOKEN = 'your_medium_integration_token'
USER_ID = 'your_user_id'

headers = {
    'Authorization': f'Bearer {MEDIUM_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'host': 'api.medium.com',
    'Accept-Charset': 'utf-8'
}

url = f'https://api.medium.com/v1/users/{USER_ID}/posts'

# Article content and metadata
data = {
    "title": "Your Article Title",
    "contentFormat": "markdown",  # Choose 'html', 'markdown', or 'plain'
    "content": "# Hello World!\nThis is my first article using the Medium API.",
    "tags": ["python", "api", "medium"],
    "publishStatus": "draft"  # Choose 'public' or 'draft'
}

# Sending the POST request
response = requests.post(url=url, headers=headers, data=json.dumps(data))

print('Status code:', response.status_code)
print('Response:', response.json())