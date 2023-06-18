from flask_restx import reqparse

person_parser = reqparse.RequestParser()
person_parser.add_argument('name', type = str)
person_parser.add_argument('age', type = str)

pet_parser = reqparse.RequestParser()
pet_parser.add_argument('name', type = str)
pet_parser.add_argument('breed', type = str)
pet_parser.add_argument('owner', type = str)