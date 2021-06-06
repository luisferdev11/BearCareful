from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = "CallateAlvAlexis"

    #from .vistas import vistas
    from .auth import auth

    #app.register_blueprint(vistas, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
