from flask import Flask
from parser import get_text_from_str, get_text_from_file, get_text_from_url

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

