from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from pandas import DataFrame
import datetime as dt
from . import mysql



def regresion(df_main, pais):
    df = df_main.query(f"pais=='{pais}'")
    X = np.array(df.year)
    y = np.array(df.depr)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)
    X_train = X_train.reshape([X_train.shape[0], 1])
    X_test = X_test.reshape([X_test.shape[0], 1])

    lr = linear_model.LinearRegression()
    lr.fit(X_train, y_train)

    Y_pred = lr.predict(X_test)

    fig = plt.figure(figsize=(3.3, 2.5))
    plt.title(f'Porcentaje de personas con depresión en {pais}')
    plt.ylabel('Porcentaje')
    plt.xlabel('Año')
    plt.scatter(X, y, c="#2EC5CE")
    plt.plot(X_test, Y_pred, c="#8C30F5", linewidth=3)

    return mpld3.fig_to_html(fig)

def usuario(id):
    data = []
    fecha = []
    #with app.app_context():
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT fec, res FROM mtest WHERE id_usu = {id}")
    myresult = cursor.fetchall()
    cursor.close()

    print(myresult)

    for row in myresult:
        fecha.append(row[0])
        data.append(int(row[1]))

    fechaDf = pd.to_datetime(fecha)
    print(fechaDf)
    fechaDf = fechaDf.map(dt.datetime.toordinal)
    X = np.array(fechaDf)
    y = np.array(DataFrame(data, columns=['puntuacion']))
    print(X)
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    X_train = X_train.reshape([X_train.shape[0], 1])
    X_test = X_test.reshape([X_test.shape[0], 1])

    lr = linear_model.LinearRegression()
    lr.fit(X_train, y_train)

    Y_pred = lr.predict(X_test)

    #Convertir el eje X en datos fecha de nuevo
    fechaDf = fechaDf.map(dt.datetime.fromordinal)
    X = np.array(fechaDf)
    print(fechaDf)
    print(X)

    #Convertir el eje x de predicciones en Datetime
    X_test = X_test.ravel()
    print(dt.datetime.fromordinal(X_test[3]))

    lenX_test = len(X_test)
    print(lenX_test)
    i=0
    X_test = X_test.astype('S')
    while i < lenX_test:
        X_test[i] = dt.datetime.fromordinal(int(X_test[i]))
        i +=1
    X_test = X_test.astype('datetime64')
    print(X_test)

    fig = plt.figure(figsize=(4, 2.5))
    plt.title('Historico test')
    plt.ylabel('Puntuacion')
    plt.xlabel('Fecha')
    #plt.plot(X, y, c="#8C30F5")
    plt.scatter(X, y, c="#2EC5CE")
    plt.plot(X_test, Y_pred, c="#8C30F5", linewidth=3)
    return mpld3.fig_to_html(fig)