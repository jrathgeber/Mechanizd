# Extracting a full list of Cryptocurrencies
# (c) 2017 QuantAtRisk.com, by Pawel Lachowicz
 
import json
from bs4 import BeautifulSoup
import requests 
 
url = "https://www.cryptocompare.com/api/data/coinlist/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
data = json.loads(soup.prettify())
data = data['Data']
 
print(data)  # display the content

crypto_lst = sorted(list(data.keys()))
print(crypto_lst)

