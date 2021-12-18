from flask import Flask
from flask_restful import Api
from controllers.file_controller import FileController
from controllers.text_controller import TextController
from controllers.url_controller import UrlController

app = Flask(__name__)
api = Api(app)

api.add_resource(TextController, '/api/v1/text')
api.add_resource(FileController, '/api/v1/file')
api.add_resource(UrlController, '/api/v1/url')

@app.route('/')
def hello_world():
    return "Hello World!!"

if __name__ == '__main__':
    app.run(debug=True)

