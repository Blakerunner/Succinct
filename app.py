import json

from flask import Flask, request
import logging
from summarizer import get_text_from_str, get_text_from_file, get_text_from_url

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/v1/file', methods=['POST'])
def post_text_summary():
    pass


@app.route('/api/v1/url', methods=['POST'])
def post_text_summary():
    pass


@app.route('/api/v1/text', methods=['POST'])
def post_text_summary():
    text = request.values.get('text')
    summary = get_text_from_str(text, 'english')[0]
    return_dict = {"text": str(summary)}
    return json.dumps(return_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
