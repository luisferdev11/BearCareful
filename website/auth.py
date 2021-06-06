from flask import Blueprint, render_template, request, url_for, redirect
from . import mysql

auth = Blueprint('auth', __name__)



@auth.route('/', methods=["GET","POST"])
def login():
    #global id
    if request.method == "POST":
        email = request.form.get('correo')
        password = request.form.get('contra')

        cursor = mysql.connection.cursor()
        query = "select id_usu from MUsuario where cor_usu = %s AND con_usu = %s"
        valores = (email, password)
        id_usu = cursor.execute(query, valores)
        cursor.close()
        return redirect(url_for('vistas.historico', id_usu=id_usu)) #Usar aqui el id obtenido
    else:
        return render_template("iniciarSesion.html")



def VerificarUsu(correo, contra):

    cursor = mysql.connection.cursor()
    query = "select id_usu from MUsuario where cor_usu = %s AND con_usu = %s"
    valores = (correo, contra)
    id_usuario = cursor.execute(query, valores)
    return id_usuario




