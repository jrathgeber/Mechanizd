# Getting a List of Cryptocurrencies sorted by their most current Market Cap
# (c) 2017 QuantAtRisk.com, by Pawel Lachowicz
# Modified and changed by Jason Rathgeber in 2020


from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from pandas.io.json import json_normalize
import configparser
import json
import time

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

apikey = config['coin']['coin.apikey']



def myformat(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')

timestr = time.strftime("%Y%m%d")
 

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'100',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

df = json_normalize(data['data'])

 
# create an empty DataFrame
#df = pd.DataFrame(columns=["Ticker","Name", "MarketCap", "Price", "Change"])
 
#for i in range(len(dic)):
#   df.loc[len(df)] = [dic[i]['symbol'], dic[i]['name'], dic[i]['market_cap'], dic[i]['price'], dic[i]['percent_change_24h']]
 
# iterating the columns 
for col in df.columns: 
    print(col) 
    


df.sort_values(by=['quote.USD.market_cap'])
# apply conversion to numeric as 'df' contains lots of 'None' string as values

#df.MarketCap = pd.to_numeric("quote.USD.market_cap")
#df.Price = pd.to_numeric(df.Price)
#P = df[df.MarketCap > 20e6]
#print(P, end="\n\n")
#portfolio = list(P.Ticker)
#print(portfolio)

myFile = open('C:\\dep\\coin\\btcmktcap.htm' ,'w')

myFile.write('<!DOCTYPE html>\n')
myFile.write('<html>\n')
myFile.write("<style media='screen' type='text/css'>");
myFile.write(".datagrid table { border-collapse: collapse; text-align: left; width: 100%; } .datagrid {font: normal 12px/150% Arial, Helvetica, sans-serif; background: #fff; overflow: hidden; border: 1px solid #006699; -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; }.datagrid table td, .datagrid table th { padding: 3px 10px; }.datagrid table thead th {background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #006699), color-stop(1, #00557F) );background:-moz-linear-gradient( center top, #006699 5%, #00557F 100% );filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#006699', endColorstr='#00557F');background-color:#006699; color:#FFFFFF; font-size: 15px; font-weight: bold; border-left: 1px solid #0070A8; } .datagrid table thead th:first-child { border: none; }.datagrid table tbody td { color: #00496B; border-left: 1px solid #E1EEF4;font-size: 12px;font-weight: normal; }.datagrid table tbody .alt td { background: #E1EEF4; color: #00496B; }.datagrid table tbody td:first-child { border-left: none; }.datagrid table tbody tr:last-child td { border-bottom: none; }.datagrid table tfoot td div { border-top: 1px solid #006699;background: #E1EEF4;} .datagrid table tfoot td { padding: 0; font-size: 12px } .datagrid table tfoot td div{ padding: 2px; }.datagrid table tfoot td ul { margin: 0; padding:0; list-style: none; text-align: right; }.datagrid table tfoot  li { display: inline; }.datagrid table tfoot li a { text-decoration: none; display: inline-block;  padding: 2px 8px; margin: 1px;color: #FFFFFF;border: 1px solid #006699;-webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #006699), color-stop(1, #00557F) );background:-moz-linear-gradient( center top, #006699 5%, #00557F 100% );filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#006699', endColorstr='#00557F');background-color:#006699; }.datagrid table tfoot ul.active, .datagrid table tfoot ul a:hover { text-decoration: none;border-color: #006699; color: #FFFFFF; background: none; background-color:#00557F;}div.dhtmlx_window_active, div.dhx_modal_cover_dv { position: fixed !important; }");
myFile.write("</style>");
myFile.write('<body>\n')
myFile.write('<h2>Data as of ['+timestr+']</h2>')
myFile.write('<div class=\'datagrid\'><table>\n')
myFile.write('<thead><tr><th>Ticker</th><th>Name</th><th>Price</th><th>Change</th><th>Cap</th></tr></thead>\n')

myFile.write('<tbody>\n') 

#for index, row in df[df.MarketCap > 20e6].iterrows():
for index, row in df.iterrows():

    myFile.write('<tr>\n')
    
    myFile.write('<td>\n')
    myFile.write(row['symbol'])
    myFile.write('</td>\n')
        
    myFile.write('<td>\n')
    myFile.write(row['name'])
    myFile.write('</td>\n')

    myFile.write('<td  align="right">\n')
    myFile.write(myformat(row['quote.USD.price']))
    myFile.write('</td>\n')

    myFile.write('<td  align="right">\n')
    myFile.write(str(row['quote.USD.percent_change_24h']))
    myFile.write('</td>\n')

    myFile.write('<td  align="right">\n')
    myFile.write(myformat(row['quote.USD.market_cap']))
    myFile.write('</td>\n')
    
    myFile.write('</tr>\n')   
   
myFile.write('</tbody>\n')      
myFile.write('</table>\n')
myFile.write('</div>\n')
myFile.write('</body>\n')
myFile.write('</html>\n')
  
myFile.close()












