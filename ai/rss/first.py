import feedparser

url = "https://www.triathlete.com/feed/"
feed = feedparser.parse(url)

print(feed)