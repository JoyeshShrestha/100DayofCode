from flask import Flask, render_template, jsonify, request,url_for
import smtplib
import os
import datetime
# from dotenv import load_dotenv
# load_dotenv()


password = os.environ["email_password"] 
my_email = os.environ["email"] 
# from flask_bootstrap import Bootstrap5
app= Flask(__name__)


# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap5(app)

def send_email(email,message):
        try:
            connection =smtplib.SMTP("smtp.gmail.com", port=587)

            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs=my_email, 
                msg=f"Subject: This is from your Portfolio\n\nemail: {email}\n\nmessage: {message}\n")
            connection.close()
            
        except:
            return False  
        else:
            return True 


@app.route('/',methods=["GET","POST"])
def hello_world():
    current_year = datetime.datetime.now().year
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        if send_email(email,message):
            return f"<h1>Successfully sent</h1><a href='{url_for('hello_world')}'>Go back</a>"
        else:
            return f"<h1>Email Failed</h1><a href='{url_for('hello_world')}'>Go back</a>"
    return render_template("index.html",year = current_year)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

@app.after_request
def add_security_headers(response):
    # Content-Security-Policy
    
    
    # X-Frame-Options
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    
    # X-Content-Type-Options
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Referrer-Policy
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    # Permissions-Policy
    response.headers['Permissions-Policy'] = 'geolocation=(self "https://yourdomain.com"), microphone=()'

    return response

if __name__ == "__main__":
    app.run(debug=False)