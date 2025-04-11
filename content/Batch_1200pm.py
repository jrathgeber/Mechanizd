
import notion.get_post as notn
import notion.search as notnsearch

from datetime import date


def do_it():

    # Get today's Date
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

        if str(key).startswith("Twitter") and str(value) != "":
            print("We will be tweeting... ")
