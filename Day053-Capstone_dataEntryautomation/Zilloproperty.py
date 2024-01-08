from bs4 import BeautifulSoup
import requests
URL = "https://appbrewery.github.io/Zillow-Clone/"
class ZilloProperty:
    def __init__(self):
        response = requests.get(URL)
        html_text = response.text
        self.soup=BeautifulSoup(html_text,"html.parser")
        self.price = 0
        self.link = ""
        self.address=""
        self.list_property = []
        self.all_info_list = []
        self.info_dict = {}
    def get_info(self):
        self.list_property = self.soup.find_all(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        for property in self.list_property:
            self.link = property.find(name="a",class_="StyledPropertyCardDataArea-anchor").get("href")
            self.address=property.find(name="address").getText()
            self.price = property.find(name="span",class_="PropertyCardWrapper__StyledPriceLine").getText()
            self.info_dict={
                "link":self.link,
                "address":self.address,
                "price":self.price
            }
            self.all_info_list.append(self.info_dict)
            