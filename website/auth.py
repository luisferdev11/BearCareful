from flask import Blueprint, render_template, request, url_for, redirect
import numpy as np
from . import mysql

auth = Blueprint('auth', __name__)



@auth.route('/', methods=["GET","POST"])
def login():
    #global id
    if request.method == "POST":
        email = request.form.get('correo')
        password = request.form.get('contra')
        print(email)
        try:
            cursor = mysql.connection.cursor()
            query = "select id_usu from MUsuario where cor_usu = %s AND con_usu = %s"
            valores = (email, password)
            print(valores)
            cursor.execute(query, valores)
            id = np.array(cursor.fetchall())
            id_usu = (id[0][0])
            cursor.close()
            return redirect(url_for('vistas.historico', id_usu=id_usu)) #Usar aqui el id obtenido
        except:
            return render_template("iniciarSesion.html")
    else:
        return render_template("iniciarSesion.html")







