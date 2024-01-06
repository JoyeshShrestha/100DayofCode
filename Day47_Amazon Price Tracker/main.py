import requests
from bs4 import BeautifulSoup
import time
Samsung_url = "https://amazon.com/SAMSUNG-32-Inch-Odyssey-FreeSync-LC32G55TQWNXZA/dp/B08FF3HDW5/ref=sr_1_15?crid=224UZK74GC5VE&keywords=monitor%2B144hz&qid=1704348154&sprefix=monitor%2B%2Caps%2C297&sr=8-15&th=1"
headers = {
    "User-Agent":"defined",
    "Accept-Language":"en-US,en;q=0.9",

}


def get_price():
    response = requests.get(url=Samsung_url,headers=headers)
    html_amazon = response.text
    soup = BeautifulSoup(html_amazon,"html.parser")

    price_element = soup.find(class_="olpWrapper a-size-small")
     
    return price_element



loop = True

while loop:
    time.sleep(2)
    getprice = get_price()
    if getprice is None:
        print("Nope")
        pass
    else:
        price=get_price.split(" ")[-1]

        print(price)
        loop=False