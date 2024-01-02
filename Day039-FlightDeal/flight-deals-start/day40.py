import os
from dotenv import load_dotenv
import requests
import smtplib


load_dotenv()
URL=os.getenv('URL')

class Day40:
    def __init__(self) -> None:
        
        self.password = os.environ["email_password"]
        self.my_email = "sjoyesh2000@gmail.com"
        self.info = {}
        self.get_info()

    def get_info(self):

            response = requests.get(url=URL)
            response.raise_for_status()
            self.info = response.json()
            

   