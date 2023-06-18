from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.sqlite3'
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app)
with app.app_context():
    from models import Persons
    db.create_all()

from routes import *