from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import ApplicationConfig
from controllers.file_controller import FileController
from controllers.text_controller import TextController
from controllers.url_controller import UrlController
from models.db import db
from controllers.user_controller.login_user_controller import LoginUserController
from controllers.user_controller.register_user_controller import RegisterUserController
from controllers.user_controller.logout_user_controller import LogoutUserController
from controllers.user_controller.current_user_controller import CurrentUserController

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
db.init_app(app)
with app.app_context():
    db.create_all()

CORS(app)
api = Api(app)

api.add_resource(TextController, '/api/v1/text')
api.add_resource(FileController, '/api/v1/file')
api.add_resource(UrlController, '/api/v1/url')
api.add_resource(LoginUserController, '/api/v1/users/login')
api.add_resource(RegisterUserController, '/api/v1/users/register')
api.add_resource(LogoutUserController, '/api/v1/users/logout')
api.add_resource(CurrentUserController, '/api/v1/users/current_user')


@app.route('/')
def hello_world():
    return "Hello World!!"


if __name__ == '__main__':
    app.run(debug=True)
