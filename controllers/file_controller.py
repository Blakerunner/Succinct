import os
from flask import request
from flask_restful import Resource, reqparse, abort
from resources.summarizer import get_text_from_file
from os.path import exists
TEMP_FILES = './files/'


class FileController(Resource):
    def get(self):
        return "This is: /api/v1/file"

    def post(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        temp_path = os.path.join(basedir, TEMP_FILES)
        if not exists(temp_path):
            os.mkdir(temp_path)

        parser = reqparse.RequestParser()
        parser.add_argument('summary_length', type=int, help='Length of the summary', required=False)
        args = parser.parse_args()
        summary_len = args['summary_length']

        if request.files:
            text_file = request.files['file']
            text_file_path = os.path.join(temp_path, text_file.filename)
            text_file.save(text_file_path)
            if summary_len:
                summary_text = get_text_from_file(text_file_path, summary_len)
            else:
                summary_text = get_text_from_file(text_file_path)
            os.unlink(text_file_path)
            return {'summary': summary_text}
        else:
            abort(400, message="file not found in post request")