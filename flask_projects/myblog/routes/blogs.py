"""Blogs Route"""

import datetime as dt
import logging

from flask import Blueprint, redirect, render_template
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from sqlalchemy.exc import SQLAlchemyError
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

from models import BlogPost, db
from schemas import BlogSchema

blogs_bp = Blueprint("blogs_bp", __name__)

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)


class NewBlogForm(FlaskForm):
    """Form for New Blog"""

    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Blog Post Subtitle", validators=[DataRequired()])
    author = StringField("Blog Author Name", validators=[DataRequired()])
    img_url = StringField(
        "Image URL", validators=[DataRequired(), URL(require_tld=True)]
    )
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    add = SubmitField("Add")


@blogs_bp.route("/")
def get_all_posts():
    """Retreive all posts"""

    data = BlogPost.query.all()
    posts = blogs_schema.dump(data)
    return render_template("index.html", all_posts=posts)


@blogs_bp.route("/show/<int:post_id>")
def show_post(post_id):
    """Display Post"""

    requested_post = BlogPost.query.get(post_id)
    print(requested_post)
    return render_template("post.html", post=requested_post)


@blogs_bp.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    """Creates new blog"""

    form = NewBlogForm()

    if form.validate_on_submit():
        new_blog = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=dt.datetime.today().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
        )

        try:
            db.session.add(new_blog)
            db.session.commit()
        except SQLAlchemyError as e:
            logging.error("Failed to add new blog: %s", e)
            db.session.rollback()
            return ("Failed to add blog: %s", {e})

        return redirect("/")

    return render_template("make-post.html", form=form)


@blogs_bp.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """Edit Post"""

    post = db.get_or_404(BlogPost, post_id)
    print(post)
    form = NewBlogForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data

        try:
            db.session.commit()
        except SQLAlchemyError as e:
            logging.error("Failed to update blog: %s", e)
            db.session.rollback()
            return ("Failed to add blog: %s", {e})

        return redirect("/")

    return render_template("make-post.html", form=form)


@blogs_bp.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    """Delete Post"""

    post = db.get_or_404(BlogPost, post_id)

    try:
        db.session.delete(post)
        db.session.commit()
    except SQLAlchemyError as e:
        logging.error("Failed to update blog: %s", e)
        db.session.rollback()
        return ("Failed to add blog: %s", {e})

    return redirect("/")


# Below is the code from previous lessons. No changes needed.
@blogs_bp.route("/about")
def about():
    """About Page"""
    return render_template("about.html")


@blogs_bp.route("/contact")
def contact():
    """Contact Page"""
    return render_template("contact.html")
