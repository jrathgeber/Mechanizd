import requests
import json
import os


import configparser

config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

token = config['notion']['token']

NOTION_TOKEN = token
DATABASE_ID = "1cfe46d2882f8052a448d6f9804be769"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def add_item(name, category, Type):
    url = f"https://api.notion.com/v1/pages"
    
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Category": {
                "select": {
                    "name": category
                }
            },
            "Type": {
                "title": Type
            }
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"Successfully added item: {name}")
    else:
        print(f"Failed to add item: {name}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")


if __name__ == "__main__":
    add_item("Example Item", "Manifest", "Conviction")