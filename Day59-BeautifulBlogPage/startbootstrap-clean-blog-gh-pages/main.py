from flask import Flask, render_template
import requests
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
if __name__=="__main__":
    app.run(debug=True)