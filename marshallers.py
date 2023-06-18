from flask_restx import fields, marshal
from models import Persons

class Add_user(fields.Raw):
    def format(self, value):
        person = Persons.query.get(int(value))
        return marshal(person, person_serializer)


person_serializer = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.String
}

pet_serializer = {
    'id': fields.Integer,
    'name': fields.String,
    'breed': fields.String,
    'owner': Add_user
}