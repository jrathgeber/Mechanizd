import requests
from bs4 import BeautifulSoup
import re

def get_product(target_url):

    l=[]
    o={}
    specs_arr=[]
    specs_obj={}

    #target_url="https://www.amazon.com/40-Week-Ironman-Step-Step-Conquering/dp/B0C5P9WYFT/?_encoding=UTF8&pd_rd_w=PuCFj&content-id=amzn1.sym.117cb3e1-fd12-46a0-bb16-15cd49babfdb%3Aamzn1.symc.abfa8731-fff2-4177-9d31-bf48857c2263&pf_rd_p=117cb3e1-fd12-46a0-bb16-15cd49babfdb&pf_rd_r=SJF9NRD53N8HBPARJ7SK&pd_rd_wg=ZOtEk&pd_rd_r=03b9aa61-afb0-4bf4-842c-d12c3816e4eb&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d"
    #target_url= "https://www.amazon.com/Hiland-Shimano-Speeds-Aluminum-Bicycle/dp/B0CMCQPYC4/"

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

    print(l)

    # result
    print("Title " + o["title"])
    print("Price " + o["price"])
    print("Rating " + o["rating"])

    return o