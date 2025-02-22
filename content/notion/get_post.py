import requests
from typing import Dict, List, Optional
import configparser

config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

token=config['notion']['token']

class NotionListExtractor:


    def get_suff(self) -> Dict:

        return self.d

    def __init__(self, token: str):

        # Make empty list
        self.d = {}

        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        self.base_url = "https://api.notion.com/v1"

    def get_page_blocks(self, page_id: str) -> List[Dict]:
        """Fetch all blocks from a Notion page."""
        url = f"{self.base_url}/blocks/{page_id}/children"
        blocks = []

        while True:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            blocks.extend(data["results"])

            if not data.get("has_more"):
                break

            url = f"{self.base_url}/blocks/{page_id}/children?start_cursor={data['next_cursor']}"

        return blocks

    def get_block_children(self, block_id: str) -> List[Dict]:
        """Fetch children of a specific block."""
        url = f"{self.base_url}/blocks/{block_id}/children"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()["results"]

    def extract_block_content(self, block: Dict) -> str:
        """Extract content from various block types."""
        block_type = block["type"]

        # Get the content object for this block type
        content = block.get(block_type, {})

        if "rich_text" in content:
            return " ".join(
                text_item["plain_text"]
                for text_item in content["rich_text"]
            )
        elif block_type == "to_do":
            checked = "☒" if content.get("checked", False) else "☐"
            return f"{checked} {self.extract_block_content({'type': 'text', 'text': content.get('rich_text', [])})}"
        elif block_type == "code":
            return f"Code ({content.get('language', 'text')}): {self.extract_block_content({'type': 'text', 'text': content.get('rich_text', [])})}"
        elif block_type == "equation":
            return f"Equation: {content.get('expression', '')}"
        elif block_type == "image":
            caption = content.get("caption", [])
            caption_text = " ".join(item["plain_text"] for item in caption) if caption else "No caption"
            return f"Image: {caption_text}"
        else:
            return f"[{block_type} block]"

    def format_block_content(self, block: Dict, indent_level: int = 0) -> str:
        """Format block content with proper indentation and structure."""
        indent = "  " * indent_level
        content = self.extract_block_content(block)

        if block["type"] == "numbered_list_item":
            return f"{indent}{content}"
        elif block["type"] == "bulleted_list_item":
            return f"{indent}• {content}"
        else:
            return f"{indent}{content}"

    def process_numbered_lists(self, page_id: str):
        """Process all numbered lists in a page and their children."""
        blocks = self.get_page_blocks(page_id)

        current_list_number = 0
        current_child_number = 0

        for block in blocks:
            if block["type"] == "numbered_list_item":
                current_list_number += 1
                content = self.extract_block_content(block)
                print(f"{current_list_number}. {content}")

                media = content

                # Process children if they exist
                if block.get("has_children"):
                    try:
                        children = self.get_block_children(block["id"])
                        for child in children:
                            child_content = self.format_block_content(child, indent_level=2)

                            print(child_content)

                            current_child_number += 1

                            post = child_content

                            self.d[media+"_"+str(current_child_number)] = post

                            # Handle nested children
                            if child.get("has_children"):
                                nested_children = self.get_block_children(child["id"])
                                for nested_child in nested_children:
                                    nested_content = self.format_block_content(nested_child, indent_level=3)
                                    print(nested_content)

                    except Exception as e:
                        print(f"Error fetching children for block {block['id']}: {e}")
            else:
                current_list_number = 0


def main(PAGE_ID) -> Dict:

    NOTION_TOKEN = token


    extractor = NotionListExtractor(NOTION_TOKEN)

    try:
        print("Processing numbered lists and their children...")
        print("--------------------------------------------")
        extractor.process_numbered_lists(PAGE_ID)

    except Exception as e:
        print(f"Error: {e}")

    print("--------------------------------------------\n")

    return extractor.get_suff()


if __name__ == "__main__":
    PAGE_ID = "1a1e46d2882f807f9ec5ff4514a2e0c1"
    test = main(PAGE_ID)
    print(test)