
from flask import Flask, render_template, request, redirect, url_for, Response, redirect
app = Flask(__name__)

import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import pymssql


connection = pymssql.connect(server="213.140.22.237\SQLEXPRESS", user="cilibeanu.nicolae",password="xxx123##",database="cilibeanu.nicolae")

@app.route('/', methods=['GET'])
def homever():
    return render_template("homeverifica.html")

@app.route('/infoUser', methods=['GET'])
def info():
    return render_template("infoUser.html")

@app.route('/rotta1', methods=['GET'])
def rotta_1():
    nome = request.args["Name"]
    cognome = request.args["Cognome"]
    query= f"select * from Sales.customers where first_name like '{nome}' and last_name like '{cognome}' " 
    df4 = pd.read_sql(query, connection)
    return render_template("rotta1.html",nomicolonne = df4.columns.values, dati = list(df4.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)