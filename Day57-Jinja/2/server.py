from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/guess/<string:name>')
def guess(name):
    para={
        "name":name
    }
    age_response = requests.get(url = "https://api.agify.io",params=para)
    age_=age_response.json()
    gender_response = requests.get(url="https://api.genderize.io",params=para)
    gender_ = gender_response.json()
    return render_template("index.html", age=age_["age"],gender=gender_["gender"],name=name.capitalize())


@app.route("/blog")
def blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_post = response.json()

    return render_template("blog.html",posts = all_post)

if __name__=="__main__":
    app.run(debug=True)

