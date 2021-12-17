from flask import Flask
from summarizer import get_text_from_str, get_text_from_file, get_text_from_url

app = Flask(__name__)

@app.route('/api/v1/file')
def succinct_file():
    return {'summary': "Summary of FILE text."}

@app.route('/api/v1/url')
def succinct_url():
    return {'summary': "Summary of URL text."}

@app.route('/api/v1/text')
def succinct_text():
    return {'summary': "Summary of TEXT text."}

@app.route('/')
def hello_world():
    return "Hello World!!"


if __name__ == '__main__':
    app.run()

