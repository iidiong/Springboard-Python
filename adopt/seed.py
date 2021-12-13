"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', species="dog",
              photo_url="https://images.dog.ceo/breeds/borzoi/n02090622_10355.jpg", age="5", available=True)
bowser = Pet(name='Bowser', species="dog",
             photo_url="https://images.dog.ceo/breeds/chow/n02112137_4447.jpg", age="6", available=False)
spike = Pet(name='Spike', species="porcupine",
            photo_url="https://images.dog.ceo/breeds/hound-walker/n02089867_1345.jpg", age="4", available=True)
tiger = Pet(name='Tiger', species="cat",
            photo_url="https://images.dog.ceo/breeds/chow/n02112137_13499.jpg", age="5", available=False)
lunah = Pet(name='Lunah', species="cat",
            photo_url="https://images.dog.ceo/breeds/maltese/n02085936_5488.jpg", age="7", available=True)
chow = Pet(name='Chow', species="porcupine",
           photo_url="https://images.dog.ceo/breeds/terrier-wheaten/n02098105_214.jpg", age="5", available=False)
dingo = Pet(name='Dingo', species="cat",
            photo_url="https://images.dog.ceo/breeds/keeshond/n02112350_7038.jpg", age="3", available=True)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)
db.session.add(tiger)
db.session.add(lunah)
db.session.add(chow)
db.session.add(dingo)

# Commit--otherwise, this never gets saved!
db.session.commit()
