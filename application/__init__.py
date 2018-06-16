from flask import Flask

from config import Config


def creat_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    from application.modules.admin import  admin_blue
    app.register_blueprint(admin_blue)

    return app