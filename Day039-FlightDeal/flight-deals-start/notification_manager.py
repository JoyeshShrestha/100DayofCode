
from day40 import Day40
from flight_data import FlightData
import smtplib
import os
import requests
from dotenv import load_dotenv
load_dotenv()
password = os.environ["email_password"]
my_email = "sjoyesh2000@gmail.com"

class NotificationManager:
    
    def __init__(self,lower_prices):
        self.lower_prices = lower_prices
        # super().__init__()
        self.send_email()
        print("hjello")


    

    def send_email(self):
        data = FlightData(self.lower_prices)
        ok_do_this =data.improve_data(self.lower_prices)    

        for i in ok_do_this: 
               
            country = i["countryTo"]
            price = i["price"]
            available = i["availability"]["seats"]
            print("-------------",country)
            information = Day40()
            info = information.info
            for i in info['users']:
                l_name = i["lastName"]
                f_name = i["firstName"]
                e_mail = i["email"]
                try:
                    connection =smtplib.SMTP("smtp.gmail.com", port=587)
                    
                    connection.starttls()
                    connection.login(user=my_email,password=password)
                    connection.sendmail(
                        from_addr = my_email, 
                        to_addrs=e_mail, 
                        msg=f"Subject: {country} has low prices\n\nGreeting {l_name}\nThere are {available} seats for the price of Rs.{price} from KTM to {country}. Have a great one\n\nRegards, JO")
                    connection.close()
                    
                except:
                    print("Email error! not sent ", e_mail)    
                else:
                    print("Email sent successfully", e_mail) 
