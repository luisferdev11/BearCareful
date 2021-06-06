from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('correo')
        password = request.form.get('contra')
        print(email)
        print(password)
    return "<p>Inicio de Sesion</p>"

@auth.route('/logout')
def logout():
    return "<p>Inicio de Sesion</p>"


def VerificarUsu(correo, contra):

    #Conectar con BD
    query = "select id_usu from MUsuario where cor_usu = %s AND con_usu = %s"
    #valores = (email, contra)
    #cursor.execute(query, valores)
    """
    try:
        email = correo
        contra = contra
        query = "select id_usu from MUsuario where cor_usu = %s AND con_usu = %s"
        valores = (email, contra)
        cursor.execute(query, valores)
        data = cursor.fetchall()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error con el usuario o password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)
    finally:
        return data
"""