from flask import Flask, render_template, request
import smtplib
import requests
import os
from dotenv import load_dotenv
load_dotenv()

password = os.environ["email_password"] 
my_email = "sjoyesh2000@gmail.com"


app=Flask(__name__)
blog_url = "https://api.npoint.io/56f9faa524d052769284"
response = requests.get(blog_url)
blog = response.json()

@app.route('/')
def get_blog():
    print(blog)
    return render_template('index.html',blog_list = blog)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts/<id>')
def get_post(id):
    return render_template('post.html',blog_post = blog[int(id) -1])


    







def send_email(name,email,phone,message):
        try:
            connection =smtplib.SMTP("smtp.gmail.com", port=587)

            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs=my_email, 
                msg=f"Subject: {name} sends you email from website\n\nname: {name}\nemail: {email}\nphone number: {phone}\nmessage: {message}\nRegards, {name} ")
            connection.close()
            
        except:
            return False  
        else:
            return True   

@app.route('/contact/success',methods = ["POST"])
def recieve_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    if send_email(name,email,phone,message):
        return f"Successfully sent"
    else:
        return f"Error while sending email"

if __name__=="__main__":
    app.run(debug=True)