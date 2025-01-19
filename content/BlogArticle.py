

# HTML content you want to save

def new_article(path, number, slug):

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My HTML Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a sample HTML page created with Python.</p>
    </body>
    </html>
    """

    # File path where you want to save the HTML file
    file_path = path + "article_" + number + "_" + slug + ".html"

    # Open the file in write mode and save the HTML content
    with open(file_path, "w") as file:
        file.write(html_content)

    print(f"HTML file saved as {file_path}")
