from flask import Flask
from resources.summarizer import get_text_from_url, get_text_from_str

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!!"


if __name__ == '__main__':
    app.run()

