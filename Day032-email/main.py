##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas
import random
import smtplib
password = "lfkh itfp sqdi xgdc" 



my_email = "sjoyesh2000@gmail.com"

files = ["./Day032-email/letter_templates/letter_1.txt","./Day032-email/letter_templates/letter_2.txt","./Day032-email/letter_templates/letter_3.txt"]
data = pandas.read_csv("./Day032-email/birthdays.csv")
dict_data = data.to_dict(orient="record")
# print(dict_data)

now = dt.datetime.now()

def send_email(data):
    file_name = random.choice(files)

    with open(file_name) as birthday:
        msg = birthday.read()
        newmsg = msg.replace('[NAME]',data['name'])
        
        try:
            connection =smtplib.SMTP("smtp.gmail.com", port=587)

            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs=data['email'], 
                msg=f"Subject: HAPPY BIRTHDAY\n\n{newmsg}")
            connection.close()
            
        except:
            print("Email error! not sent")    
        else:
            print("Email sent successfully")


for i in dict_data:
    if i["month"] == now.month:
        if i["day"] == now.day:
            send_email(i)


