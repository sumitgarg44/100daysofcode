from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.exc import SQLAlchemyError
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

BASEDIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASEDIR, "instance/users.db")

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":
        hash_password = generate_password_hash(request.form["password"], method="pbkdf2", salt_length=8)
        new_user = User(
            email=request.form["email"],
            password=hash_password,
            name=request.form["name"],
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash(f"Successfully completed Sign up", "success" )
            return render_template("secrets.html", name=request.form["name"])
        except SQLAlchemyError as e:
            flash(f"Sign up failed with error: {e}", "danger" )
            return render_template("register.html")

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    login_fail = ""

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("secrets"))
        
        login_fail = flash("Incorrect username or password", "danger")

    return render_template("login.html", message=login_fail)

@app.route('/secrets')
@login_required
def secrets():
    name = ""

    is_logged_in = current_user.is_authenticated

    if is_logged_in:
        name = current_user.name
    
    return render_template("secrets.html", name=name, logged_in=is_logged_in)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/download')
@login_required
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
