
import notion.get_post as notn
import notion.search as notnsearch
import youtubevids.upload_video
import twitter.tweet
import content.ai.Perplexity as perp

from datetime import timedelta
from datetime import date

# Get today's Date
today = date.today() - timedelta(days=0)
formatted_date = today.strftime("%Y%m%d")
print("Processing " + formatted_date)

# Get the Notion page ID
url = notnsearch.search_notion_page(formatted_date)
print(url)

if url is None:
    print (f"Date {formatted_date} not in Notion pages. Check connections.")
    exit()

page_id = url.partition("-")[2]

# Connect to Notion and get today's Journal
daily_dict = notn.main(page_id)

# Do the business
for key, value in daily_dict.items():

    print(f"{key}:{value}")

    if str(key).startswith("Twitter") and str(value) != "":

        post = perp.get_latest_info(value)
        # twitter.tweet.tweetSomething(post)
        print("Tweeting ::: " + post)
