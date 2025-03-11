import content.ai.OpenAi01 as Ai


def new_article(path, number, slug, key_words, further_info):

    html_content_2 = Ai.write_article(key_words, further_info)

    # File path where you want to save the HTML file
    file_path = path + "article_" + number + "_" + slug + ".html"

    # Open the file in write mode and save the HTML content
    with open(file_path, "w") as file:
        file.write(html_content_2)

    print(f"HTML file saved as {file_path}")

    return html_content_2
