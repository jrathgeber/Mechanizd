import concurrent.futures as cf
from  context import timer
import requests

URL = "https://www.google.com/"


def get(url: str):
    response = requests.get(url)

    return response.content


# Initiate a timer
with timer():
    # Initiate a pool
    with cf.ThreadPoolExecutor() as tpe:
        for index, _ in enumerate(range(100), 1):
            tpe.submit(get, URL)

#This code block executed in 7.929 seconds.