
from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm
from forms import EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def list_pets():
    """ Display all pets on homepage """
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Add a new pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet_form(id):
    """Edit a pet"""
    form = EditPetForm()
    pet = Pet.query.get_or_404(id)

    form.photo_url.value = pet.photo_url
    form.notes.value = pet.notes
    form.available.value = pet.available

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        if(form.available.data == "True"):
            pet.available = True
        else:
            pet.available = False

        pet = Pet(photo_url=pet.photo_url,
                  notes=pet.notes, available=pet.available)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet_form.html",  pet=pet, form=form)
