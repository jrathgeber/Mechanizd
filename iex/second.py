import pandas as pd
import requests
from datetime import datetime as dt

import configparser

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

api_key = config['finazon']['key']

page_no = [0, 1, 2, 3, 4]
data_dict = []


# Get list of data sets
sets_json = requests.get(f'https://api.finazon.io/latest/datasets?apikey={api_key}').json()
print(sets_json)



for i in page_no:
    hist_json = requests.get(

        f'https://api.finazon.io/latest/time_series?publisher=sip&ticker=AAPL&interval=1d&page={i}&page_size=1000&order=desc&apikey={api_key}').json()['data']

        # f'https://api.finazon.io/latest/time_series?publisher=sip&ticker=AAPL&interval=1d&page={i}&page_size=1000&order=desc&apikey={api_key}').json()
        # f'https://api.finazon.io/latest/datasets?apikey={api_key}').json()



    print(hist_json)
    #data_dict.append(hist_json)

aapl_df = pd.DataFrame(columns=['t', 'o', 'h', 'l', 'c', 'v'])

for i in range(0, len(data_dict)):
    df = pd.DataFrame(data_dict[i])
    aapl_df = aapl_df.append(df, ignore_index=True)

aapl_df = aapl_df[::-1].reset_index(drop=True)
aapl_df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
aapl_df.Date = pd.to_datetime(aapl_df.Date.astype(int), unit='s').dt.date
aapl_df.tail()