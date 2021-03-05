from flask import Flask, render_template, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


connect_db(app)

@app.route('/')
def homepage():
    """Home page for pet adoption agency"""

    pets = db.session.query(Pet.id, Pet.name, Pet.photo_url, Pet.available)

    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet_form():
    """Form to create a new pet"""
    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # if the user didn't enter a url, use a default cartoon img of cat
        if photo_url != "":   
            photo_url = form.photo_url.data
        else: 
            photo_url ="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg"

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet_form(id):
    """Edit pet form with prepopulated values for selected pet"""

    pet = Pet.query.get(id)
    form = AddPetForm(obj=pet) # get pet data and pre-populate values in form

    if form.validate_on_submit():

        pet.name = form.name.data
        pet.species = form.species.data
        
        pet.photo_url = form.photo_url.data
        if pet.photo_url != "":
            pet.photo_url = form.photo_url.data
        else: 
            pet.photo_url ="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg"
       
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()

        return redirect("/")

    else:
        return render_template('edit_pet.html', form=form)

