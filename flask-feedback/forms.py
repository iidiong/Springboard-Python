""" This form is user to generate input fields in html form """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired


class RegisterUserForm(FlaskForm):
    """ Create Register user form"""

    first_name = StringField("FirstName", validators=[InputRequired()])
    last_name = StringField("LastName", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class LoginUserForm(FlaskForm):
    """ Login Registered user form"""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    
class FeedbackForm(FlaskForm):
    """ Login Registered user form"""
    title = StringField("Title", validators=[InputRequired()])
    content = StringField("Content", validators=[InputRequired()])
    # content = TextAreaField("Content", render_kw={"rows": 3, "cols": 11}, validators=[InputRequired()])
    # username = StringField("Username", validators=[InputRequired()])
