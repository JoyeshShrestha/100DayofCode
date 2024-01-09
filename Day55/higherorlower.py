from flask import Flask
import random
app = Flask(__name__)

correct = random.randint(0,9)



@app.route("/")
def main_page():
    return "<h1>Guess a number between 0 and 9</h1>"\
"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:number>")
def match(number):
    if number==correct:
            return f"<h1>This is Correct</h1>"\
            "<img src='https://media0.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif?cid=ecf05e47f6qxu838am09cunfb222p05n4n6pv66tfirtppyf&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif number<correct:
            return f"<h1>This is low</h1>"\
            "<img src='https://media4.giphy.com/media/5i7umUqAOYYEw/giphy.gif?cid=ecf05e47f6qxu838am09cunfb222p05n4n6pv66tfirtppyf&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    else:
            return f"<h1>This is high</h1>"\
            "<img src='https://media0.giphy.com/media/C9x8gX02SnMIoAClXa/giphy.gif?cid=ecf05e47f6qxu838am09cunfb222p05n4n6pv66tfirtppyf&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"


if __name__ == "__main__":
    app.run(debug=True)