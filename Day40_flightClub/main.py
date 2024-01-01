import os
from dotenv import load_dotenv
import requests
import smtplib


load_dotenv()
password = os.environ["email_password"]
my_email = "sjoyesh2000@gmail.com"
URL=os.getenv('URL')

response = requests.get(url=URL)
response.raise_for_status()
info = response.json()
print(info)
for i in info["users"]:
    try:
                connection =smtplib.SMTP("smtp.gmail.com", port=587)
                
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(
                    from_addr = my_email, 
                    to_addrs=i[email], 
                    msg=f"Subject: {country} has low prices\n\nGreeting\nThere are {available} seats for the price of Rs.{price} from KTM to {country}. Have a great one\nRegards, JO")
                connection.close()