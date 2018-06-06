# third-party imports
from flask_restful import Api

# local imports
from app import create_app
from app.resources.users import Users

app = create_app()

api = Api(app)
api.add_resource(Users, '/users', '/users/<string:id>', endpoint='users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
