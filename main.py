from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

"""
Lazily with the factory pattern

from flask import Flask
from flask_restx import Api

api = Api()
app = Flask(__name__)
api.init_app(app)
"""

@api.route('/hello', '/world')
class HelloWord(Resource):
    def get(self):
        return {'hello': 'world TCS'}
    
if __name__ == '__main__':
    app.run(debug=True)