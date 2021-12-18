import os
import werkzeug
from flask import request
from flask_restful import Resource, reqparse, abort
from resources.summarizer import get_text_from_file

class FileController(Resource):
    def get(self):
        return "This is: /api/v1/file"

    def post(self):
        if request.files:
            text_file = request.files['file']
            text_file_path = os.path.join('./files/', text_file.filename)
            text_file.save(text_file_path)
            summary_text = get_text_from_file(text_file_path)
            os.unlink(text_file_path)
            return {'summary': summary_text}
        else:
            abort(400, message="text field not found in post request")