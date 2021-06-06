from flask import Blueprint, render_template
from .graficas import regresion, usuario, pd

vistas = Blueprint('vistas', __name__)


@vistas.route('/historico/<id_usu>')
def historico(id_usu):

    return render_template("historico.html", historico=usuario(id=id_usu))

@vistas.route('/paises')
def paises():
    columnas = ("pais", "year", "depr")
    df_main = pd.read_csv("datadepression.csv", header=0)
    df_main.columns = columnas
    return render_template("paises.html",CAN=regresion(df_main, "CAN"), MEX=regresion(df_main, "MEX"), USA=regresion(df_main, "USA"))