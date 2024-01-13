from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()
with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all() 


    

@app.route('/')
def home():
    
    return render_template('index.html',books = all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        book_name = request.form['bookname']
        author = request.form['author']
        rating = request.form['rating']
        book = {
            "title":book_name,
            "author":author,
            "rating":rating,
        }
        all_books.append(book)
        with app.app_context():
            new_book = Book(title=book_name, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()   
        return redirect(url_for('home'))


@app.route("/<id>",methods=["GET","POST"])
def edit(id):
    if request.method == "GET":
        # all_books[id]
        # book_p=all_books[int(id)-1]
        # print(id)
        # print("----",book_p["title"])
        with app.app_context():
            book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            title = book.title
            rating = book.rating
            author = book.author
        return render_template('edit.html',title=title,rating=rating,author=author)
    elif request.method == "POST":
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)  
            book_to_update.title = "Harry Potter and the Goblet of Fire"
            db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)

