
from flight_data import FlightData
import smtplib
import os
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
            available = i["availability"]
            print("-------------",country)
            try:
                connection =smtplib.SMTP("smtp.gmail.com", port=587)
                
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(
                    from_addr = my_email, 
                    to_addrs=my_email, 
                    msg=f"Subject: {country} has low prices\n\nGreeting\nThere are {available} seats for the price of Rs.{price} from KTM to {country}. Have a great one\nRegards, JO")
                connection.close()
                
            except:
                print("Email error! not sent")    
            else:
                print("Email sent successfully") 