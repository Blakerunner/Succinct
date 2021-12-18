from flask_restful import Resource, reqparse, abort
from resources.summarizer import get_text_from_str

class TextController(Resource):
    def get(self):
        return "This is: /api/v1/text"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, help='Text to be summarized', required=True)
        parser.add_argument('summary_length', type=int, help='Length of the summary', required=False)
        args = parser.parse_args()
        if args['text']:
            text = args['text']
            if args['summary_length']:
                summary_text = get_text_from_str(text, args['summary_length'])
            else:
                summary_text = get_text_from_str(text)
            return {'summary': summary_text}
        else:
            abort(400, message="text field not found in post request")