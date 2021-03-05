from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    
    name = StringField("Pet Name", 
        validators=[InputRequired(message="Pet Name can't be blank Yo!")])
    species = SelectField("Species", 
        validators=[InputRequired(message="Species can't be blank")], 
        choices=[('cat', 'cat'), ('dog', 'dog'), ('fish', 'fish')])
    photo_url = StringField("Photo URL", 
        validators=[Optional(), URL(require_tld=True, message="Must be a valid URL")])
    age = IntegerField("Pet Age", 
        validators=[NumberRange(min=0, max=30, message="Age in years must be between 0 and 30")])
    notes = StringField("Pet Description")
