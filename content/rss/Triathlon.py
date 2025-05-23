import feedparser

url = "https://www.triathlete.com/feed/"
feed = feedparser.parse(url)

print(feed)

print("Feed Title:", feed.feed.title)
print("Feed Description:", feed.feed.description)
print("Feed Link:", feed.feed.link)

for entry in feed.entries:
    print("Entry Title:", entry.title)
    print("Entry Link:", entry.link)
    print("Entry Published Date:", entry.published)
    print("Entry Summary:", entry.summary)
    print("\n")


from datetime import datetime, timedelta, timezone

# Define the time range (e.g., the last 24 hours)
now = datetime.now(timezone.utc)
time_range = timedelta(days=1)

# Iterate through entries and filter by the time range
for entry in feed.entries:
    entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    if now - entry_date <= time_range:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published Date:", entry.published)
        print("Entry Summary:", entry.summary)
        print("\n")