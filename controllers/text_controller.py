from flask_restful import Resource

class TextController(Resource):
    def get(self):
        return "This is: /api/v1/url"

    def post(self):
        return {'summary': "Summary of TEXT text."}