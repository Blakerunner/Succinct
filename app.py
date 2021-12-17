from flask import Flask
from resources.summarizer import get_text_from_url

app = Flask(__name__)


@app.route('/')
def hello_world():
    get_text_from_url("https://hi.wikipedia.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0")
    return "Hello World!!"


if __name__ == '__main__':
    app.run()

