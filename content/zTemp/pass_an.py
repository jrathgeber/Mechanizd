import openai
import os
from datetime import datetime
from bs4 import BeautifulSoup

openai.api_key = os.environ.get("OPENAI_API_KEY")

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def update_article(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    article_text = soup.get_text()

    prompt = f"""
    Update the following article based on current events, especially the first paragraph. 
    Mention that stocks have been crashing in the last few days due to Trump's tariffs being bigger than expected. 
    Include today's date ({datetime.now().strftime('%Y-%m-%d')}) in the update.

    Original article:
    {article_text[:4000]}  # Limit to first 4000 characters to fit within token limits

    Updated article:
    """

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    updated_text = response.choices[0].text.strip()
    
    first_paragraph = soup.find('p')
    if first_paragraph:
        first_paragraph.string = updated_text

    return str(soup)

def main():
    file_path = "blogpost_025_will_the_stock_market_crash.html"
    html_content = read_html_file(file_path)
    updated_html = update_article(html_content)

    with open("updated_" + file_path, "w", encoding="utf-8") as file:
        file.write(updated_html)

    print("Article updated and saved as 'updated_" + file_path + "'")

if __name__ == "__main__":
    main()