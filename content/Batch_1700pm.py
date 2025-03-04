
import mediun.create_article
import notion.get_post as notn
import notion.search as notnsearch
import twitter.tweet

from datetime import date

# Get todays Date
today = date.today()
formatted_date = today.strftime("%Y%m%d")
print("Processing " + formatted_date)

# Get the Notion page ID
url = notnsearch.search_notion_page(formatted_date)
page_id = url.partition("-")[2]

# Connect to Notion and get today's Journal
daily_dict = notn.main(page_id)

for key, value in daily_dict.items():
    print(f"{key}: {value}")

    if str(key).startswith("Twitter") and str(value) != "":
        #twitter.tweet.tweetSomething(value)
        print("Tweeting ::: " + value)

    if str(key).startswith("Medium") and str(value) != "":
        mediun.create_article.do_it(value)

keyword = "how to get a post from notion via python api"
