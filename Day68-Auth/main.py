from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        user_name = request.form["name"]
        try:
            email = request.form.get('email')
            result = db.session.execute(db.select(User).where(User.email == email))
            user = result.scalar()
            if user:
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('login'))
            register = User(
            name = user_name,
            email = email,
            password = generate_password_hash(request.form["password"],method='pbkdf2:sha256',salt_length=8)
            )
            db.session.add(register)
            db.session.commit()
        except:
            return redirect(url_for("login"))

        login_user(register)
        return redirect(url_for("secrets",name=user_name))

        
    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if not user:
            flash("That email does not exist, please try again.")
            # return redirect(url_for('login'))
        elif not check_password_hash(user.password,password):
            flash("Incorrect Password!")
        else:
            login_user(user)
            

            return redirect(url_for('secrets'))
    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html",name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("index.html",logged_in=False)


@app.route('/download')
@login_required
def download():
    return send_from_directory('static',
        path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
