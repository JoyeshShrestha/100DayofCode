#This class is responsible for talking to the Flight Search API.

import os
import requests
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
KIWI_FLIGHT_URL = "https://api.tequila.kiwi.com/v2/search"
load_dotenv()
class FlightSearch:
    def __init__(self):
        self.is_lower=False

        pass
    def get_flight_info(self,list_IATA:dict):
        today=datetime.now()
        date_from =today.strftime(f"%d/%m/%Y")
        date_to = (date.today() + timedelta(6*365/12))
        date_to = date_to.strftime(f"%d/%m/%Y")

        print(f"{date_from}..............{date_to}")
        header = {
            "apikey":os.environ["KIWI_FLIGHT_API"]
        }

        
        # list_I.append("/".join(list_IATA))
        # print("------------",list_I)
        lower_prices = []
        cities = {}
        for key,value in list_IATA.items():
            query = {
                "fly_from":"KTM",
                "fly_to": key,
                "date_from":str(date_from),
                "date_to":str(date_to),
                "one_for_city": 1,
                "curr":"NPR"

            }
            
            kiwi_responses = requests.get(url=KIWI_FLIGHT_URL,params=query,headers=header)
            kiwi_responses.raise_for_status()
            flight_data =kiwi_responses.json()
            already_city_list = [ ]
            
            for flights in flight_data["data"]:
                

                city =flights["cityCodeTo"]

                if city in already_city_list:
                    continue


                
                already_city_list.append(city)
                price = flights["price"]
                print(f"{city}.....{price}.....v{value}")

                if price<value:
                    lower_prices.append(flights)
                    self.is_lower = True

                cities[city] = price
                # break
            
            # cities.append(city_lists)
            # lowest_prices = [city,price for (city,price) in city_dict.items()]
                
        
        return cities,self.is_lower,lower_prices

