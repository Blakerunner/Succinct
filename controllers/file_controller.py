from flask_restful import Resource

class FileController(Resource):
    def get(self):
        return "This is: /api/v1/file"

    def post(self):
        return {'summary': "Summary of FILE text."}