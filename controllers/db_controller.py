import json

from flask_restful import Resource
from flask import session

from models.user import User


class DBController(Resource):
    def get(self):
        user_id = session.get("user_id")

        if not user_id:
            return {"error": "Unauthorized"}, 401

        user = User.query.filter_by(id=user_id).first()
        return {
            "id": user.id,
            "queries": json.loads(user.queries)
        }

    def post(self):
        return "USE GET: api/v1/users/queries"
