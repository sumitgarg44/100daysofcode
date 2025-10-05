"""Cafes API"""

import logging
import os

from flask import Flask, render_template

from models import db
from routes.cafes import cafes_bp

# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = Flask(__name__)
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(ROOTDIR, "cafes.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
db.init_app(app)

# Register blueprint
app.register_blueprint(cafes_bp)

# Create db is not exist
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """Home Page"""

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
