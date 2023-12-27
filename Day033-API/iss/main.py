import requests
import smtplib
from datetime import datetime
password = "lfkh itfp sqdi xgdc" 



my_email = "sjoyesh2000@gmail.com"






MY_LAT = 51.507351 # Your latitude
MY_LONG  = -0.127758 # Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5<= iss_latitude <=MY_LAT+5 and MY_LONG-5<= iss_latitude <= MY_LONG+5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <=sunrise:
        return True

if is_iss_overhead() and is_night():
    try:
            connection =smtplib.SMTP("smtp.gmail.com", port=587)

            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs="joyesh.shrestha@thamescollege.edu.np", 
                msg=f"Subject: LOOK UP\n\n ISS is above")
            
            connection.close()
            
    except:
            print("Email error! not sent")    
    else:
            print("Email sent successfully")    

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



