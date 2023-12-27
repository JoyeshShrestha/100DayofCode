import requests
from twilio.rest import Client
import os

account_sid = "AC3aa4f88b8d618ba059571ae8cefa7e6a"
auth_token = "15599d53c838666392b79bdaecf09c5d"
API_KEY = "2d7b96792fae3a3fae5989bc4d585b12"
MY_LAT = 27.717245
MY_LONG = 85.323959

parameters = {
    "lat" : MY_LAT,
    "lon": MY_LONG,
    "cnt":4,
    "appid" : API_KEY
}

# ?q=${s}&APPID=2d7b96792fae3a3fae5989bc4d585b12&units=${toggle}
response = requests.get("http://api.openweathermap.org/data/2.5/weather",params=parameters)

response.raise_for_status()

weather_data = response.json()

id = weather_data['weather'][0]['id']

code = os.environ["API_TWILLIO"]

will_rain = False
if id <=700:
    will_rain = True

# if will_rain:
#     client = Client(account_sid,auth_token)

#     message = client.messages \
#             .create(
#                 body="Its going to rain today. Rmember to bring umbrella",
#                 from ="+15017122661",
#                 to = "+9779843375283"
#             )    

