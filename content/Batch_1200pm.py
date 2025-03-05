
import notion.get_post as notn
import notion.search as notnsearch
import youtub.upload_video

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

# Do the business
for key, value in daily_dict.items():
    print(f"{key}: {value}")

    if str(key).startswith("YouTube") and str(value) != "":

        path = "F:\\Photos\\Videos_2024\\20241017_155213.mp4"
        youtub.upload_video.upload_video_from_batch(path, value)
