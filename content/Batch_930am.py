import time
import configparser
import yahoo.sendMail as sm
import twitter.tweet as tw
import web.get_gainers as tv
import content.ai.Perplexity as perp

config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

gdurl = config['godaddy']['godaddy.url']
gduser = config['godaddy']['godaddy.user']
gdpass = config['godaddy']['godaddy.pass']

url = config['yahoo']['yahoo.url']
user = config['yahoo']['yahoo.user']
password = config['yahoo']['yahoo.pass']
server = config['yahoo']['yahoo.server']
port = config['yahoo']['yahoo.port']
username = config['yahoo']['yahoo.username']

daterun = time.strftime("%Y%m%d")
print(daterun)

# dummy list
tickerList = ['AXSM', 'VIPS']
print(tickerList)

# all gainers
allpriceslist = tv.get_stock_gainers()

# top 5
n = 5
gainers = allpriceslist.get("Ticker")
tickerList = gainers[:n]

# make the report with perplexity
post = perp.get_gainers_info('$' + ', $'.join(tickerList))

print(post)

print ("In here")
for _, row in allpriceslist.iterrows():
    print(f"{row['Ticker']} ({row['Company']}): {row['Gain']}")

if tickerList[0]=='error':
    sm.send_mail('jrathgeber@yahoo.com', 'jrathgeber@yahoo.com', 'Max List ' + ''.join(tickerList), ''.join(tickerList), [], server, port, username, password)
else:
    # SC.getSymbolConfig(tickerList, daterun, maxdata)
    sm.send_mail(user, user, 'Max ' + ','.join(tickerList), '$' + ', $'.join(tickerList) + ' \n \n Brought to you by https://www.mechanizd.com',[], server, port, username, password)
    #Tweet.tweetSomething('Equity day trade algo focus list $' + ', $'.join(tickerList) + ' \n \n Brought to you by https://www.mechanizd.com')
    #sendMail.send_mail(user, user, 'Max ' + ','.join(tickerList), ', $'.join(tickerList) + '',[], server, port, username, password)

    tw.tweetSomething('Testing : Equity pre market gainers $' + ', $'.join(tickerList) + ' Further details  : \n' + post)

    print("We sent and tweeted all we could")