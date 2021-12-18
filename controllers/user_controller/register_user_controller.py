from flask_restful import Resource, reqparse, abort
from flask import jsonify, session
from models.user import User, db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class RegisterUserController(Resource):
    def get(self):
        return "This is: api/v1/users/register"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help='User Email needed', required=True)
        parser.add_argument('password', type=str, help='Password needed', required=True)
        args = parser.parse_args()
        if args['email'] and args['password']:
            email = args['email']
            password = args['password']
            user_exists = User.query.filter_by(email=email).first() is not None

            if user_exists:
                return jsonify({"error": "User already exists"}), 409

            hashed_password = bcrypt.generate_password_hash(password)
            new_user = User(email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            session["user_id"] = new_user.id

            return jsonify({
                "id": new_user.id,
                "email": new_user.email
            })
        else:
            abort(400, message="text field not found in post request")