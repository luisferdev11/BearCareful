from website import create_app



app = create_app()

"""
# Configurar DB

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_PORT'] = db['mysql_port']
mysql = MySQL()

mysql.init_app(app)
"""
if __name__ == '__main__':
    app.run(debug=True)