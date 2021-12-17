from flask_restful import Resource

class TextController(Resource):
    def get(self):
        return "This is: /api/v1/url"

    def post(self):
        return {'summary': "Summary of TEXT text."}

    # def post_text_summary():
    #     text = request.values.get('text')
    #     summary = get_text_from_str(text, 'english')[0]
    #     return_dict = {"text": str(summary)}
    #     return json.dumps(return_dict)