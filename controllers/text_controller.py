from flask_restful import Resource, reqparse


class TextController(Resource):
    def get(self):
        return "This is: /api/v1/text"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, help='Text to be summarized', required=True)
        args = parser.parse_args()
        if args['text']:
            text = args['text']
            summary_text = self.text_summary(text)
            return {'summary': summary_text}
        else:
            abort(400, message="text field not found in post request")

    def text_summary(self, text: str):
        return text[:15].split()