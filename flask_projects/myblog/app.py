"""My Blog"""

import logging
import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor

from models import db
from routes.blogs import blogs_bp

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = Flask(__name__)
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(ROOTDIR, "instance/posts.db")

app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
db.init_app(app)
Bootstrap5(app)
ckeditor = CKEditor(app)
app.register_blueprint(blogs_bp)

# Create DB if doesn't exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
