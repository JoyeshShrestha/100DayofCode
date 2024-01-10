from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)
post=Post()
@app.route('/')
def home():
    
    return render_template("index.html",blog_post=post.blog)

@app.route('/post/<id>')
def get_blog(id):
    blogs = post.blog
    return render_template("post.html",blog_post = blogs[int(id)])
if __name__ == "__main__":
    app.run(debug=True)
