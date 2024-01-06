url="https://www.daraz.com.np/products/fantech-mk876-mechanical-blue-switch-keyboard-i124682292-s1033871313.html?spm=a2a0e.searchlist.sku.61.57a15cc2iObC3k&search=1"

import requests
from bs4 import BeautifulSoup
import time
daraz_url="https://www.daraz.com.np/products/fantech-mk876-mechanical-blue-switch-keyboard-i124682292-s1033871313.html?spm=a2a0e.searchlist.sku.61.57a15cc2iObC3k&search=1"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9",


}


def get_price():
    response = requests.get(url=daraz_url,headers=headers,stream=True)
    

    # with open('website.html', 'wb') as file:
    #     for chunk in response.iter_content(chunk_size=8192):
    #         file.write(chunk)
    
    for chunk in response.iter_content(chunk_size=8192):
        soup = BeautifulSoup(chunk,"html.parser")
        price_element = soup.select_one("#module_product_price_1")
        print(price_element)
    # html_daraz = response.text
    # print("okok")
    # print(html_daraz)
    # soup = BeautifulSoup(html_daraz,"html.parser")
    # print(soup.title)
    # price_element = soup.select_one("#module_product_price_1 div div span").get()
    
     
    # print(price_element)



get_price()