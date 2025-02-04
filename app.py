from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import ApplicationConfig
from controllers.db_controller import DBController
from controllers.file_controller import FileController
from controllers.text_controller import TextController
from controllers.url_controller import UrlController
from models.db import db
from controllers.user_controller.login_user_controller import LoginUserController
from controllers.user_controller.register_user_controller import RegisterUserController
from controllers.user_controller.logout_user_controller import LogoutUserController
from controllers.user_controller.current_user_controller import CurrentUserController

app = Flask(__name__)
app.secret_key = "1234"
app.config.from_object(ApplicationConfig)
db.init_app(app)
with app.app_context():
    db.create_all()

cors = CORS(app, supports_credentials=True)
api = Api(app)

app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

api.add_resource(TextController, '/v1/text')
api.add_resource(FileController, '/v1/file')
api.add_resource(UrlController, '/v1/url')
api.add_resource(LoginUserController, '/v1/users/login')
api.add_resource(RegisterUserController, '/v1/users/register')
api.add_resource(LogoutUserController, '/v1/users/logout')
api.add_resource(CurrentUserController, '/v1/users/current_user')
api.add_resource(DBController, '/v1/users/queries')


@app.route('/')
def base_url():
    return "Succinct API!!"


if __name__ == '__main__':
    app.run(debug=True)
