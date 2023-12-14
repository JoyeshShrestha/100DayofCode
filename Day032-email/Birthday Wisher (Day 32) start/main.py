import smtplib
import datetime as dt
import pandas

import random
password = "lfkh itfp sqdi xgdc" 



my_email = "sjoyesh2000@gmail.com"







def send_quotes():
    with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day032-email\\Birthday Wisher (Day 32) start\\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        all_quotes =[quote.strip() for quote in all_quotes]
        selected_quotes = random.choice(all_quotes)
        # print(all_quotes)

        try:
            connection =smtplib.SMTP("smtp.gmail.com", port=587)

            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs="joyesh.shrestha@thamescollege.edu.np", 
                msg=f"Subject: Quotes of the day\n\n{selected_quotes}\nRegards, JO")
            connection.close()
            
        except:
            print("Email error! not sent")    
        else:
            print("Email sent successfully")    

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 3:
    send_quotes()