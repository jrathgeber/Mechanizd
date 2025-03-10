# https://hackernoon.com/automate-your-writing-publishing-to-medium-with-python-and-the-medium-api

import requests
import json
import configparser


def do_it(idea, content):
    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    # Replace with your actual Medium integration token and user ID
    MEDIUM_TOKEN = config['medium']['access']
    USER_ID = config['medium']['user']

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
        "title": f'{idea}',
        "contentFormat": "markdown",  # Choose 'html', 'markdown', or 'plain'
        "content": f'{content}',
        "tags": ["python", "api", "medium"],
        "publishStatus": "draft"  # Choose 'public' or 'draft'
    }

    # Sending the POST request
    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    print('Status code:', response.status_code)
    print('Response:', response.json())


if __name__ == "__main__":
    do_it('My first day', "It was a great day but it rained")
