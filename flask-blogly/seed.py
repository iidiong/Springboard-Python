""" Seed file to make sample data"""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# if table is not empty empty it

User.query.delete()

# add users
John = User(first_name="John", last_name="Idiong", image_url="")
Emmanuel = User(first_name="Emmanuel", last_name="Idiong", image_url="")
Edison = User(first_name="Edison", last_name="Idiong", image_url="")

db.session.add(John)
db.session.add(Emmanuel)
db.session.add(Edison)

db.session.commit()
