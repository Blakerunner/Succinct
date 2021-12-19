from flask_cors import cross_origin
from flask_restful import Resource, reqparse, abort
from flask import session
from models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class LoginUserController(Resource):
    def get(self):
        return "USE POST: api/v1/users/login"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help='User Email needed', required=True)
        parser.add_argument('password', type=str, help='Password needed', required=True)
        args = parser.parse_args()
        if args['email'] and args['password']:
            email = args['email']
            password = args['password']
            user = User.query.filter_by(email=email).first()

            if user is None:
                abort(401, message="Unauthorized")

            if not bcrypt.check_password_hash(user.password, password):
                abort(401, message="Unauthorized")

            session["user_id"] = user.id
            session.permanent = True

            return {
                "id": user.id,
                "email": user.email
            }
        else:
            abort(400, message="text field not found in post request")