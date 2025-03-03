import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

token=config['notion']['token']

def search_notion_page(query):
    """
    Searches for a Notion page by title using the Notion API.

    Args:
        notion_token: Your Notion API token.
        query: The title of the page to search for.

    Returns:
        The page object if found, None otherwise.
    """
    url = "https://api.notion.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "query": query,
        "filter": {
            "property": "object",
            "value": "page"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    results = response.json()["results"]

    if results:
        return results[0].get("url")
    else:
        return None

# Example usage
page_title = "20250228"

page = search_notion_page(page_title)

if page:
    print(json.dumps(page, indent=2))
else:
    print(f"Page with title '{page_title}' not found.")