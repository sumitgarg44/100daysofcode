"""Database Models"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """SQL Base class"""

    pass  # pylint: disable=unnecessary-pass


db = SQLAlchemy(model_class=Base)


# CONFIGURE TABLE
class BlogPost(db.Model):  # pylint: disable=too-few-public-methods
    """BlogPost DB Class"""

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
