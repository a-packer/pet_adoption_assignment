"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

leonard = Pet(name='Leonard', species="cat", photo_url="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg", age=2)
liz = Pet(name='Liz', species="cat", photo_url="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg", age=2 )
maggie = Pet(name='Maggie', species="fish", photo_url="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg", age=2)
fluffy = Pet(name='Fluffy', species="dog", photo_url="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg", age=12, available=False)
sandy = Pet(name='Sandy', species="dog", photo_url="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg", age=2)
puff = Pet(name='Puff', species="fish", photo_url="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg", age=20, available=False)



db.session.add_all([leonard, liz, maggie, fluffy, sandy, puff])
db.session.commit()
