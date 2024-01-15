from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

ckeditor = CKEditor()
ckeditor.init_app(app)
# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class AddBlogForm(FlaskForm):
    title=StringField("Blog Title")
    subtitle=StringField("Subtitle")
    author=StringField("Author's name")
    img_url = StringField("Image URL")
    body = CKEditorField('Body')
    submit = SubmitField("Done") 



with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    blog = db.session.execute(db.select(BlogPost))
    posts = blog.scalars().all()
    print(posts)
    # posts = []
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    # requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
    requested_post = db.get_or_404(BlogPost,post_id)
    print(requested_post)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post',methods=['GET','POST'])
def add_new_post():
    form = AddBlogForm()
    if form.validate_on_submit():
        now = datetime.now()
        
        date_formated = now.strftime("%B %d,%Y")
        with app.app_context():
            new_cafe = BlogPost(
                title=request.form.get("title"),
                subtitle=request.form.get("subtitle"),
                date=date_formated,
                body=request.form.get("body"),
                author=request.form.get("author"),
                img_url=(request.form.get("img_url")),
                )
            db.session.add(new_cafe)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html",form = form,title="New Post")
# TODO: edit_post() to change an existing blog post
@app.route("/edit/<blog_id>",methods=['GET','POST'])
def edit_post(blog_id):
    post = db.get_or_404(BlogPost,blog_id)
    edit_form =AddBlogForm(
        title=post.title,
        subtitle=post.subtitle,
        date=post.date,
        img_url=post.img_url,
        author=post.author,
        body=post.body
)
    if request.method == 'POST':
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data    
        
        db.session.commit()
        return redirect(url_for('show_post',post_id = blog_id))
   
    return render_template('make-post.html',form=edit_form,title="Edit Existing Post")
# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
        blog = db.get_or_404(BlogPost,post_id)
        db.session.delete(blog)
        db.session.commit() 
        return redirect(url_for('get_all_posts'))
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
