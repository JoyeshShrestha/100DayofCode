import requests
from datetime import datetime 
MY_LAT = 27.717245
MY_LONG = 85.323959
time_now = datetime.now()

parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":1,

}
response = requests.get("https://api.sunrisesunset.io/json",params=parameters)

response.raise_for_status()
data=response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(time_now.hour)


