import blog.write_blog
import mediun.create_article
import mediun.write_article
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

#Medium String builder
med_list = []
title = ""

for key, value in daily_dict.items():
    print(f"{key}: {value}")

    if str(key).startswith("Blog") and str(value) != "":
        blog.write_blog.write(value)

    if str(key).startswith("Medium") and str(value) != "":
        if "Article : " in str(value):
            title = value.partition("Article : ")[2]
        med_list.append(value)

    if str(key).startswith("Twitter") and str(value) != "":
        #twitter.tweet.tweetSomething(value)
        print("Tweeting ::: " + value)


my_ideas = "".join(med_list)

print("The text : ")
print (med_list)

content = mediun.write_article.new_article(title, my_ideas)

print("Title : " + title)
print("Content : " + content)

mediun.create_article.do_it(title, content)

