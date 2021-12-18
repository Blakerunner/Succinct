import logging
import werkzeug
from flask_restful import Resource, reqparse, abort
from resources.summarizer import get_text_from_file


class FileController(Resource):
    def get(self):
        return "This is: /api/v1/file"

    def post(self):
        parse = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', help='Text to be summarized', required=True)
        args = parser.parse_args()
        text_file = args['file']
        if args['text']:
            text = args['text']
            summary_text = self.text_summary(text)
            return {'summary': summary_text}
        else:
            abort(400, message="text field not found in post request")
