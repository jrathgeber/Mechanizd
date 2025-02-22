import requests
from bs4 import BeautifulSoup

import html5lib

# URL of the page to parse
page_url = "https://polite-slug-2c9.notion.site/20250221-1a1e46d2882f807f9ec5ff4514a2e0c1"

# Keywords to extract sections for
keywords = [
    "Beehive",
    "JR",
    "Open AI",
    "Claude",
    "Gemini",
    "Grok",
    "LinkedIn",
    "Medium",
    "Triathlon",
    "Twitter",
    "Youtube"
]

# Function to fetch and parse the text content from a webpage
def fetch_page_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html5lib')
    #soup = BeautifulSoup(response.content, "lxml")

    return soup.get_text(separator=' ', strip=True)


# Function to fetch and parse the text content from a webpage
def fetch_page_content_ns(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")

    #soup = BeautifulSoup(response.content, "html.parser")
    #soup = BeautifulSoup(response.content, "lxml")

    return response.content



# Function to extract specific sections by keywords
def extract_sections(text, keywords):
    sections = {key: "" for key in keywords}
    for key in keywords:
        if key in text:
            start = text.find(key)
            end = text.find('\n', start)
            sections[key] = text[start:end].strip() if end != -1 else text[start:].strip()
    return sections

# Main execution
if __name__ == "__main__":

#    page_text = fetch_page_content_ns(page_url)
#    extracted_sections = extract_sections(page_text, keywords)
#    print(page_text)

    page_text_parse = fetch_page_content(page_url)
    extracted_sections = extract_sections(page_text_parse, keywords)
    #print(page_text_parse)
    print(extracted_sections)

    # Save extracted sections
    with open("extracted_sections.txt", "w") as output_file:
        for section, content in extracted_sections.items():
            output_file.write(f"{section}:{content}\n")

    print("Sections successfully extracted and saved as 'extracted_sections.txt'")