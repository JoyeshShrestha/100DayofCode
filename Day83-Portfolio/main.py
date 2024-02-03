from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app= Flask(__name__)


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)