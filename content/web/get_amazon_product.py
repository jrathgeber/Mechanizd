import requests
from bs4 import BeautifulSoup
import re

def get_product(target_url):

    l=[]
    o={}
    specs_arr=[]
    specs_obj={}

    headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

    resp = requests.get(target_url, headers=headers)
    print(resp.status_code)
    if(resp.status_code != 200):
        print(resp)
    soup=BeautifulSoup(resp.text,'html.parser')


    try:
        o["title"]=soup.find('h1',{'id':'title'}).text.lstrip().rstrip()
    except:
        o["title"]=None


    images = re.findall('"hiRes":"(.+?)"', resp.text)
    o["images"]=images

    try:
        o["price"]=soup.find("span",{"class":"a-price"}).find("span").text
    except:
        o["price"]=None


    try:
        o["rating"]=soup.find("i",{"class":"a-icon-star"}).text
    except:
        o["rating"]=None


    specs = soup.find_all("tr",{"class":"a-spacing-small"})

    for u in range(0,len(specs)):
        spanTags = specs[u].find_all("span")
        specs_obj[spanTags[0].text]=spanTags[1].text


    specs_arr.append(specs_obj)
    o["specs"]=specs_arr
    l.append(o)

    specs_str = str(o["specs"])

    print(l)

    # result
    print("Title " + o["title"])
    print("Price " + o["price"])
    print("Rating " + o["rating"])
    print("Rating " + specs_str)

    return o