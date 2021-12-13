from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """ Form for adding pet."""
    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """ Form for Editing pet."""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = StringField("Available", validators=[Optional()])
