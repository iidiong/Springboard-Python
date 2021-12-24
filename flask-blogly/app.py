"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User, Post
from datetime import date, datetime

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "2cc9fae98fdb5fd816cb5681f370b6d7"

connect_db(app)
db.create_all()


@app.route("/")
def root():
    return redirect("/users")


@app.route("/users")
def list_all_users():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("index.html", users=users)


@app.route("/users/new")
def add_user_form():
    return render_template("new_user.html")


@app.route("/users/new", methods=["POST"])
def add_new_user():
    """Add user and redirect to list"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user = User(first_name=first_name,
                last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect("/")


@app.route("/users/<int:user_id>")
def display_user_detail(user_id):

    post = Post.query.filter(Post.user_id == user_id).all()
    if post:
        return render_template("user_page.html", posts=post)
    else:
        flash("You need to add a post")
        return redirect(f"/users/{user_id}/posts/new")
        
@app.route("/users/<int:user_id>/edit")
def display_edit_user_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user_edit.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user_form(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]
    db.session.add(user)
    db.session.commit()
    return redirect("/users")


@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>/posts/new")
def show_post(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("new_post_form.html", user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_new_post(user_id):
    title = request.form["title"]
    content = request.form["content"]
    created_at = datetime.now()
    user_id = user_id
    
    post = Post(title=title, content=content, created_at=created_at, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return redirect('/')

@app.route("/posts/<int:post_id>")
def show_a_post(post_id):
    post = Post.query.filter(post_id==post_id).first()
    return render_template("post_detail_page.html", post=post)

@app.route("/posts/<int:post_id>/edit")
def show_post_edit_form(post_id):
    post = Post.query.filter(post_id==post_id).first()
    return render_template("edit_post.html", post=post)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def save_edited_post(post_id):
    post = Post.query.filter(post_id == post_id).first()
    post.title = request.form.get("title")
    post.content = request.form.get("content")
    post = Post(title=post.title, content=post.content)
    db.session.commit()
    return redirect("/")


@app.route("/posts/<int:post_id>/delete")
def delete_a_post(post_id):
    post = Post.query.filter(post_id == post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{post.user_id}")
