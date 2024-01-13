from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# class Base(DeclarativeBase):
#   pass
# db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projectmovie.db"

# db.init_app(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)



class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year:Mapped[int] = mapped_column(Integer, nullable=False)
    description:Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250),nullable=False)

with app.app_context():
    db.create_all()

# with app.app_context():

#             second_movie = Movie(
#                     title="Avatar The Way of Water",
#                     year=2022,
#                     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#                     rating=7.3,
#                     ranking=9,
#                     review="I liked the water.",
#                     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#                 )  
#             db.session.add(second_movie)
#             db.session.commit()  
with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.id))
        all_movies = result.scalars().all() 
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")



class AddMovieForm(FlaskForm):
    title=StringField("Movie Title")
    year=StringField("Year")
    description=StringField("Describe the movie")
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    ranking = StringField("what is the ranking")

    review = StringField("Your Review")
    img_url = StringField("Image URL")

    submit = SubmitField("Done")    
@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.id))
        all_movies = result.scalars().all() 
        return render_template("index.html",movies = all_movies)

@app.route("/update/<id>",methods=["GET", "POST"])
def update(id):
     form = RateMovieForm()
     
     movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    #  movie = db.get_or_404(Movie, id)
            
     if form.validate_on_submit():
        with app.app_context():
            movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
            
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))
     return render_template("edit.html",movie=movie,form=form)

@app.route("/<id>")
def delete(id):
    with app.app_context():
            movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
            db.session.delete(movie)
            db.session.commit() 
    return redirect(url_for('home'))

@app.route("/add",methods = ['GET','POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        with app.app_context():
            new_movie = Movie(title=form.title.data, year=form.year.data, description=form.description.data,
                    rating=form.rating.data,
                    ranking=form.ranking.data,
                    review=form.review.data,
                    img_url=form.img_url.data)
            db.session.add(new_movie)
            db.session.commit() 
        return redirect(url_for('home'))
    return render_template("add.html",form=form)
        

if __name__ == '__main__':
    app.run(debug=True)
