from flask import Flask
from flask_mysqldb import MySQL
import yaml

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.secret_key = "CallateAlvAlexis"

    db = yaml.load(open('db.yaml'))
    app.config['MYSQL_HOST'] = db['mysql_host']
    app.config['MYSQL_USER'] = db['mysql_user']
    app.config['MYSQL_PASSWORD'] = db['mysql_password']
    app.config['MYSQL_DB'] = db['mysql_db']
    app.config['MYSQL_PORT'] = db['mysql_port']
    mysql.init_app(app)

    from .vistas import vistas
    from .auth import auth

    app.register_blueprint(vistas, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app

