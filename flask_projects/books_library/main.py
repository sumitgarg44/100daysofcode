from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float
from sqlalchemy.exc import SQLAlchemyError
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASEDIR, "books.db")

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Book(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author, "review": self.review}
    

app = Flask(__name__)
app.secret_key = "SuperSecretKey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DB_FILE)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    books = db.session.scalars(db.select(Book).order_by(Book.title))
    all_books = [b.to_dict() for b in books]
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            review = request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id)

    if request.method == "POST":
        new_review = request.form.get("new_review")

        if new_review:
            try:
                book.review = float(new_review)
                db.session.commit()
                return redirect(url_for("home"))
            except ValueError:
                return "Invalid rating!", 400
            
    return render_template("edit.html", book=book)

@app.route("/delete/<int:book_id>", methods=["POST"])
def delete(book_id):
    book = db.get_or_404(Book, book_id)

    try:
        db.session.delete(book)
        db.session.commit()
        flash("Book delete successfully!", "success")
    except SQLAlchemyError as e:
        db.session.rollback()
        flash("Failed to delete book!", "danger")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

