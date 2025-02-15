# Fetch Current Weather
# pip install requests-html
import requests
from bs4 import BeautifulSoup
import tweet

city = "NewYork"
url = "https://www.google.com/search?q=weather+in+" + city
req = requests.get(url)
html = BeautifulSoup(req.text, "html.parser")# Fetch Temperature
temp = html.find("div", attrs={"class": "BNeawe"}).text
print("Temp: ", temp)# Fetch Weather
weather = html.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
print("Weather: ", weather)
tweet.tweetSomething("Good Morning NYC: " + weather)
