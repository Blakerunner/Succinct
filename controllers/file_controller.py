import logging

import werkzeug
from flask_restful import Resource, reqparse, abort
from resources.summarizer import get_text_from_file


class FileController(Resource):
    def get(self):
        return "This is: /api/v1/file"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        if args['file']:
            file = args['file']
            with open(file, 'r') as infile:
                return {'summary': "summary_text"}
        else:
            abort(400, message="text field not found in post request")
