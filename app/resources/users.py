# third-party imports
from flask_restful import Resource, reqparse, fields, marshal_with

# local imports
from app import db
from app.models import User
from app.common.resource_type import email

parser = reqparse.RequestParser()
parser.add_argument(
    'firstName', dest='first_name',
    location='json', type=str,
    required=True, help='First Name cannot be empty!'
)
parser.add_argument(
    'lastName', dest='last_name',
    location='json', type=str,
    required=True, help='Last Name cannot be empty!'
)
parser.add_argument(
    'email', location='json',
    type=email, required=False
)


user_fields = {
    'id': fields.Integer(default=0),
    'firstName': fields.String(attribute='first_name'),
    'lastName': fields.String(attribute='last_name'),
    'email': fields.String(attribute='email'),
    'date_created': fields.DateTime(dt_format='iso8601'),
    'date_updated': fields.DateTime(dt_format='iso8601'),
    '_links': {
        'self': {
            'href': fields.Url('users', absolute=True)
        }
    }
}


class Users(Resource):

    @marshal_with(user_fields)
    def get(self, id):
        """
        Returns the user information for the given user ID.
        :param id: User id
        :return: User info
        """

        user = User.query.filter_by(id=id).first_or_404()

        return user

    @marshal_with(user_fields)
    def post(self):
        """
        Saves and returns the given user information.
        :return: User info
        """

        args = parser.parse_args()

        user = User(
            first_name=args.first_name,
            last_name=args.last_name,
            email=args.email)

        db.session.add(user)
        db.session.commit()

        return user, 201

    @marshal_with(user_fields)
    def put(self, id):
        """
        Updates and returns the given user information.
        :param id: User id
        :return: User info
        """

        args = parser.parse_args()

        user = User.query.filter_by(id=id).first_or_404()

        user.first_name = args.first_name
        user.last_name = args.last_name
        user.email = args.email

        db.session.commit()

        return user

    def delete(self, id):
        """
        Deletes a user for the given user ID.
        :param id: User id
        :return: no content
        """

        user = User.query.filter_by(id=id).first_or_404()

        db.session.delete(user)
        db.session.commit()

        return '', 204
