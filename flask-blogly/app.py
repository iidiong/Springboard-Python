"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

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
    return render_template("newuser.html")


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
    user = User.query.get_or_404(user_id)
    return render_template("userDetail.html", user=user)


@app.route("/users/<int:user_id>/edit")
def display_edit_user_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("userEdit.html", user=user)


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
