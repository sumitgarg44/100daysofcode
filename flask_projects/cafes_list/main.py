"""Cafes List"""

import csv
import os

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAFE_CSV = os.path.join(BASE_DIR, "cafe-data.csv")

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

coffee_rating_choices = [n * "☕" for n in range(1, 6)]
wifi_rating_choices = [n * "💪" for n in range(1, 6)]
wifi_rating_choices.insert(0, "✘")
power_rating_choices = [n * "🔌" for n in range(1, 6)]
power_rating_choices.insert(0, "✘")


class CafeForm(FlaskForm):
    """Cafe form class"""

    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open_time = StringField("Opening Time e.g. 9AM", validators=[DataRequired()])
    close_time = StringField("Closing Time e.g. 10PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating", validators=[DataRequired()], choices=coffee_rating_choices
    )
    wifi_rating = SelectField(
        "Wifi Rating", validators=[DataRequired()], choices=wifi_rating_choices
    )
    power_rating = SelectField(
        "Power Rating", validators=[DataRequired()], choices=power_rating_choices
    )
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    """Home Page"""
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    """Adds a new cafe"""
    form = CafeForm()
    if form.validate_on_submit():
        with open(CAFE_CSV, mode="a", encoding="utf-8") as file:
            new_cafe = (
                f"\n{form.cafe.data},"
                f"{form.location.data},"
                f"{form.open_time.data},"
                f"{form.close_time.data},"
                f"{form.coffee_rating.data},"
                f"{form.wifi_rating.data},"
                f"{form.power_rating.data}"
            )
            file.write(new_cafe)
            return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    """List of cafes"""
    with open(CAFE_CSV, newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
