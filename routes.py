from flask_restx import Resource, marshal
from flask import jsonify, Response
from main import api, db
from models import Persons, Pets
from rest_parser import person_parser, pet_parser
from marshallers import person_serializer, pet_serializer
import json

@api.route("/person")
class Person(Resource):

    def get(self):
        persons = Persons.query.all()
        return jsonify(status = 200, persons = marshal(persons, person_serializer))
    
    def post(self):
        req_body = person_parser.parse_args()
        
        user_already_exits = Persons.query.filter_by(name = req_body['name']).first()

        if user_already_exits:
            res = Response(
                response =  json.dumps({"message": "User Already Exists."}),
                status = 400
            )
            return res
        
        person = Persons(
            name = req_body['name'],
            age = req_body['age']
        )

        db.session.add(person)
        db.session.commit()

        return jsonify(status = 201, person = marshal(person, person_serializer))

@api.route("/person/<int:id>")
class OnePerson(Resource):

    def get(self, id):
        user_already_exits = Persons.query.get(id)
        
        if user_already_exits:  
            return jsonify(person = marshal(user_already_exits, person_serializer), status = 200)
        else:
            res = Response(
                response =  json.dumps({"message": "User Not Found."}),
                status = 400
            )
            return res
        
    def delete(self, id):
        user_already_exits = Persons.query.get(id)
        
        if user_already_exits:  

            db.session.delete(user_already_exits)
            db.session.commit()

            res = Response(
                response =  json.dumps({"message": "User Successfuly Deleted."}),
                status = 200
            )
            return res
        else:
            res = Response(
                response =  json.dumps({"message": "User Not Found."}),
                status = 400
            )
            return res

    def put(self, id):
        user_already_exits = Persons.query.get(id)
        req_body = person_parser.parse_args()
        if user_already_exits: 
            req_body = {k: v for k, v in req_body.items() if v != None} 
            Persons.query.filter_by(id = id).update(req_body)
            db.session.commit()
            return jsonify(person = marshal(user_already_exits, person_serializer), status = 200)
        else:
            res = Response(
                response =  json.dumps({"message": "User Not Found."}),
                status = 400
            )
            return res

@api.route("/pet")
class Pet(Resource):

    def get(self):
        pets = Pets.query.all() 
        return jsonify(pets = marshal(pets, pet_serializer), status = 200)
    
    def post(self):
        req_body = pet_parser.parse_args()
        person = Persons.query.get(int(req_body['owner']))

        pet = Pets(
            name = req_body['name'],
            breed = req_body['breed'],
            persons = person
        )

        db.session.add(pet)
        db.session.commit()

        return jsonify(pet = marshal(pet, pet_serializer), status = 201)
