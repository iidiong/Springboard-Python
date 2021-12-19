
from flask import Flask, redirect, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Feedback
from forms import RegisterUserForm, LoginUserForm, FeedbackForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "This is a secrete"


connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route("/")
def user():
    return redirect("/register")


@app.route("/register")
def show_register_page():
    """ This function display register user form """
    form = RegisterUserForm()
    return render_template("register.html", form=form)


@app.route("/register", methods=["POST"])
def create_new_user():
    """ This function create a new user in db """
    form = RegisterUserForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        
        user = User.register(username, password, email, first_name, last_name)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append("Username is taken. Please pick another one")
            return render_template("register.html", form=form)
        session["username"] = username
        flash(f"Thank you {username} for your registration")
        return redirect(f"/users/{username}")
    
    else:
        return redirect("/register")


@app.route("/login")
def show_login_page():
    form = LoginUserForm()
    return render_template("login.html", form=form)


@app.route("/login", methods=["POST"])
def user_login():
    form = LoginUserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session["username"] = username
            return redirect(f"/users/{username}")
        else:
            form.username.errors = ["Bad name/password"]
    return redirect("/login")


@app.route("/logout")
def logout():
    """ Logs user out and redirect to homepage """
    # session.pop("username")
    session.clear()
    return redirect("/")


@app.route("/users/<username>")
def show_user_info(username):
    if "username" not in session:
        flash("You must be logged in to view")
        return redirect("/login")

    flash(f"Success Welcome {username}!")
    all_feedbacks = Feedback.query.all()
    return render_template("user_profile.html", feedbacks=all_feedbacks, username=username)


@app.route("/users/<username>/delete", methods=["POST"])
def delete_user(username):
    if "username" not in session:
        flash("You must be logged in to delete account")
        return redirect('/login')
    else:
        user = User.query.filter_by(username=username).first()
        # session.pop(user.username)
        db.session.delete(user)
        db.session.commit()
        flash(f"Account successfully deleted { username}")
        session.clear()
        return redirect('/')


@app.route("/users/<username>/feedback/add")
def add_feedback(username):
    if session["username"] != username:
        return redirect("/login")
    else:
        form = FeedbackForm()
        return render_template("new_feedback.html", form=form, username=username)


@app.route("/feedback/<int:feedback_id>/update")
def show_edit_feedback(feedback_id):
    form = FeedbackForm()
    feedback = Feedback.query.get_or_404(feedback_id)

    form.title.value = feedback.title
    form.content.value = feedback.content

    return render_template("edit_feedback.html", form=form)


@app.route("/feedback/<int:feedback_id>/update", methods=["POST"])
def edit_feedback(feedback_id):
    username = session['username']
    form = FeedbackForm()
    feedback = Feedback.query.get_or_404(feedback_id)

    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data
        Feedback(title=feedback.title, content=feedback.content)
        db.session.commit()
        return redirect(f"/users/{username}")


@app.route("/users/<username>/feedback/add", methods=["POST"])
def show_feedback_form(username):
    form = FeedbackForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        username = username

        feedback = Feedback(title=title, content=content, username=username)
        db.session.add(feedback)
        db.session.commit()
        return redirect(f"/users/{username}")
    else:
        return redirect(f"/users/{username}/feedback/add")


@app.route("/feedback/<int:feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    db.session.delete(feedback)
    db.session.commit()
    username = session['username']
    return redirect(f"/users/{username}")
