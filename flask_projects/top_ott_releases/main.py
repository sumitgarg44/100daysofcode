"""All time favourite releases"""

import os

import requests
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# CREATE DB
BASEDIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASEDIR, "database.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """SQLAlchemy Base class"""

    pass  # pylint: disable=unnecessary-pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Release(db.Model):  # pylint: disable=too-few-public-methods
    """Releases Table"""

    __tablename__ = "releases"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    review: Mapped[str] = mapped_column(String(150), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class RatingForm(FlaskForm):
    """Rating Form"""

    rating = StringField(
        "Your rating",
        render_kw={"placeholder": "Enter a rating between 1 and 10"},
        validators=[DataRequired()],
    )
    review = StringField(
        "Your review",
        render_kw={"placeholder": "Enter a review"},
        validators=[DataRequired()],
    )
    submit = SubmitField("Done")


class FindReleaseForm(FlaskForm):
    """Add Release Form"""

    new_release_title = StringField("Release Title", validators=[DataRequired()])
    submit = SubmitField("Add Release")


### TMDB Variables
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_GETBYID_URL = "https://api.themoviedb.org/3/movie"
TMDB_APIKEY = os.environ.get("API_TOKEN")

TMDB_HEADERS = {"accept": "application/json", "Authorization": f"Bearer {TMDB_APIKEY}"}


@app.route("/")
def home():
    """Home page"""

    all_releases = db.session.scalars(
        db.select(Release).order_by(Release.rating.asc())
    ).all()
    return render_template("index.html", releases=all_releases)


@app.route("/edit/<int:release_id>", methods=["GET", "POST"])
def edit(release_id):
    """Edit Rating"""

    release = db.get_or_404(Release, release_id)
    form = RatingForm()

    if request.method == "POST":
        if form.validate_on_submit():
            try:
                release.rating = float(form.rating.data)
                release.review = str(form.review.data)
                db.session.commit()
                flash("Rating and review updated successfully!", "success")
                return redirect(url_for("home"))
            except SQLAlchemyError:
                flash("Rating and review failed to update!", "danger")
                return redirect(url_for("home"))
        else:
            flash("Form validation failed. Check your input.", "warning")
            return redirect(url_for("home"))

    return render_template("edit.html", release=release, form=form)


@app.route("/delete/<int:release_id>", methods=["POST"])
def delete(release_id):
    """Delete OTT Release"""

    release = db.get_or_404(Release, release_id)

    try:
        db.session.delete(release)
        db.session.commit()
        flash("OTT release has been deleted successfully!", "success")
        return redirect(url_for("home"))
    except SQLAlchemyError:
        flash("Failed to delete release!", "danger")
        return redirect(url_for("home"))


@app.route("/find", methods=["GET", "POST"])
def find():
    """Find OTT Release to later add into DB"""

    form = FindReleaseForm()

    if request.method == "POST":
        new_release_title = str(form.new_release_title.data)
        try:
            response = requests.get(
                TMDB_SEARCH_URL,
                params={"query": new_release_title},
                headers=TMDB_HEADERS,
                timeout=60,
            )
            response.raise_for_status()
        except requests.HTTPError as http_err:
            return f"error: Upstream API returned an error: {http_err}", 502
        except requests.RequestException as req_err:
            return f"error: Network error while contacting upstream API: {req_err}", 503

        data = response.json()
        return render_template("select.html", releases=data["results"])

    return render_template("add.html", form=form)


@app.route("/add/<int:release_id>", methods=["POST"])
def add(release_id):
    """Add OTT Release into DB"""

    try:
        response = requests.get(
            f"{TMDB_GETBYID_URL}/{release_id}", headers=TMDB_HEADERS, timeout=60
        )
        response.raise_for_status()
    except requests.HTTPError as http_err:
        return f"error: Upstream API returned an error: {http_err}", 502
    except requests.RequestException as req_err:
        return f"error: Network error while contacting upstream API: {req_err}", 503

    data = response.json()
    new_release = Release(
        title=data["title"],
        year=int(data["release_date"].split("-")[0]),
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
    )

    try:
        db.session.add(new_release)
        db.session.commit()
        flash("OTT release has been added successfully!", "success")
        return redirect(url_for("edit", release_id=new_release.id))
    except SQLAlchemyError:
        flash("Failed to add release!", "danger")
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
