from main import db

class Persons(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    age = db.Column(db.String(2))
    pet = db.relationship("Pets", backref = 'persons')
    car = db.relationship("Cars", backref = 'persons')
    def __repr__(self):
        return f"{self.id} | {self.name} | {self.age}"
    
class Pets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    breed = db.Column(db.String(200))
    owner = db.Column(db.Integer, db.ForeignKey('persons.id'))

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    brand = db.Column(db.String(200))
    mileage = db.Column(db.Float)
    owner = db.Column(db.Integer, db.ForeignKey('persons.id'))