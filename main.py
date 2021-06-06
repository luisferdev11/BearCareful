from flask import Flask
#from website import create_app
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
app.secret_key = "CallateAlvAlexis"

from website import vistas
from website import auth

app.register_blueprint(vistas, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

#Aqui comenzaba
#app = create_app()


# Configurar DB
mysql = MySQL()
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_PORT'] = db['mysql_port']

mysql.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)