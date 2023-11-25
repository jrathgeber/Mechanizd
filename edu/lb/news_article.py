#!pip install newspaper3k

from newspaper import Article
url = "http://cnn.com/2023/03/29/entertainment/the-mandalorian-episode-5-recap/index.html"
article = Article(url)
article.download()
article.parse()
print(article.text)