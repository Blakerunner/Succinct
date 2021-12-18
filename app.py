from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_cors import CORS
from config import ApplicationConfig
from controllers.file_controller import FileController
from controllers.text_controller import TextController
from controllers.url_controller import UrlController
from models.user import User, db

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
db.init_app(app)
with app.app_context():
    db.create_all()

bcrypt = Bcrypt(app)
CORS(app)
api = Api(app)

api.add_resource(TextController, '/api/v1/text')
api.add_resource(FileController, '/api/v1/file')
api.add_resource(UrlController, '/api/v1/url')

@app.route('/')
def hello_world():
    return "Hello World!!"

if __name__ == '__main__':
    app.run(debug=True)

