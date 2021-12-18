from flask_restful import Resource, reqparse, abort
from resources.summarizer import get_text_from_url

class UrlController(Resource):
    def get(self):
        return "This is: /api/v1/url"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str, help='Url to be summarized', required=True)
        parser.add_argument('summary_length', type=int, help='Length of the summary', required=False)
        args = parser.parse_args()
        if args['url']:
            url = args['url']
            if args['summary_length']:
                summary_text = get_text_from_url(url, args['summary_length'])
            else:
                summary_text = get_text_from_url(url)
            return {'summary': summary_text}
        else:
            abort(400, message="url field not found in post request")

