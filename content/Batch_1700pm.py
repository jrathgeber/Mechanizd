import blog.write_blog
import mediun.create_article
import mediun.write_article
import notion.search as notnsearch
import notion.get_post as notn
import twitter.tweet
import youtube.upload_video
import wordpress.Blog_tri1

from datetime import date

# Get today's Date
today = date.today()
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

# Medium String builder
med_list = []
title = ""

# Flags for running it. Makes easier to test.
blog_flag = False
medium_flag = False
triathlon_flag = False
twitter_flag = False
youtube_flag = False

#Iterate the list
for key, value in daily_dict.items():

    print(f"{key}: {value}")

    if str(key).startswith("Blog") and str(value) != "" and blog_flag:
        blog.write_blog.write(value)

    if str(key).startswith("Medium") and str(value) != "" and medium_flag:
        if "Article : " in str(value):
            title = value.partition("Article : ")[2]
        med_list.append(value)

    if str(key).startswith("Triathlon") and str(value) != "" and triathlon_flag:
        wordpress.Blog_tri1.create_blog_post(value)

    if str(key).startswith("Twitter") and str(value) != "" and twitter_flag:
        twitter.tweet.tweetSomething(value)
        print("Tweeting ::: " + value)

    if str(key).startswith("YouTube") and str(value) != "" and youtube_flag:
        path = "F:\\Photos\\Videos_2024\\20241017_155213.mp4"
        youtube.upload_video.upload_video_from_batch(path, value)

if medium_flag:

    my_ideas = "".join(med_list)

    print("The text : ")
    print(med_list)

    content = mediun.write_article.new_article(title, my_ideas)

    print("Title : " + title)
    print("Content : " + content)

    mediun.create_article.do_it(title, content)

print("finished batch")
