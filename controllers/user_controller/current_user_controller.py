from flask_restful import Resource
from flask import session
from models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class CurrentUserController(Resource):
    def get(self):
        user_id = session.get("user_id")

        if not user_id:
            return {"error": "Unauthorized"}, 401

        user = User.query.filter_by(id=user_id).first()
        return {
            "id": user.id,
            "email": user.email
        }

    def post(self):
        return "Use GET: api/v1/users/current_user"
