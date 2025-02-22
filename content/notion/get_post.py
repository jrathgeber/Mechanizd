import os
import json
import requests
import argparse
from datetime import datetime


class NotionPageDownloader:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        self.base_url = "https://api.notion.com/v1"

    def get_page_content(self, page_id):
        """Retrieve the content of a Notion page."""
        blocks_url = f"{self.base_url}/blocks/{page_id}/children"

        response = requests.get(blocks_url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Failed to get page content: {response.text}")

        return response.json()

    def get_page_title(self, page_id):
        """Retrieve the title of a Notion page."""
        page_url = f"{self.base_url}/pages/{page_id}"

        response = requests.get(page_url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Failed to get page title: {response.text}")

        return response.json()

    def format_block_content(self, block):
        """Format the content of a block based on its type."""
        block_type = block['type']

        if block_type not in block:
            return ""

        content = block[block_type]

        if block_type == "paragraph":
            return self._get_rich_text(content.get('rich_text', []))
        elif block_type == "heading_1":
            return f"\n# {self._get_rich_text(content.get('rich_text', []))}\n"
        elif block_type == "heading_2":
            return f"\n## {self._get_rich_text(content.get('rich_text', []))}\n"
        elif block_type == "heading_3":
            return f"\n### {self._get_rich_text(content.get('rich_text', []))}\n"
        elif block_type == "bulleted_list_item":
            return f"• {self._get_rich_text(content.get('rich_text', []))}\n"
        elif block_type == "numbered_list_item":
            return f"1. {self._get_rich_text(content.get('rich_text', []))}\n"
        elif block_type == "to_do":
            checkbox = "☒" if content.get('checked', False) else "☐"
            return f"{checkbox} {self._get_rich_text(content.get('rich_text', []))}\n"
        elif block_type == "code":
            return f"\n```{content.get('language', '')}\n{self._get_rich_text(content.get('rich_text', []))}\n```\n"
        elif block_type == "quote":
            return f"> {self._get_rich_text(content.get('rich_text', []))}\n"
        elif block_type == "divider":
            return "\n---\n"
        else:
            return f"[Unsupported block type: {block_type}]\n"

    def _get_rich_text(self, rich_text):
        """Extract text from rich_text array."""
        return "".join(text.get('plain_text', '') for text in rich_text)


def main():
    parser = argparse.ArgumentParser(description="Download and display Notion page content")
    parser.add_argument("page_id", help="Notion page ID")
    parser.add_argument("--save", action="store_true", help="Save content to a file")
    parser.add_argument("--format", choices=["text", "markdown"], default="markdown",
                        help="Output format (default: markdown)")

    args = parser.parse_args()

    try:
        # Check for token
        token = os.environ.get("NOTION_TOKEN")
        if not token:
            raise ValueError("Please set the NOTION_TOKEN environment variable")

        # Initialize downloader
        downloader = NotionPageDownloader(token)

        # Get page title and content
        page_info = downloader.get_page_title(args.page_id)
        page_content = downloader.get_page_content(args.page_id)

        # Format content
        formatted_content = []
        for block in page_content['results']:
            formatted_block = downloader.format_block_content(block)
            if formatted_block:
                formatted_content.append(formatted_block)

        content = "\n".join(formatted_content)

        # Save content if requested
        if args.save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"notion_page_{timestamp}.{args.format}"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"\nContent saved to: {filename}")

        # Print content
        print("\nPage Content:\n")
        print(content)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()