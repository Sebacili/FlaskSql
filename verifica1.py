#Realizzare un sito web cyhe permetta di visualizzare tutti i dipendenti che lavorano in un certo store.
#Il maneger inserisce il nome dello store e clicca su un bottone che invia i dati al server. 
#Quest'ultimo accede al database e restituisce i nomi e i cognomi dei dipendenti di quello store. 
#Se il nome dello store non è presente, deve essere restituito un opportuno messaggio di errore. Tutta la parte grafica deve essere gestita con Bootstrap.

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
    return render_template("homeverifica1.html")

@app.route('/ricerca', methods=['GET'])
def ricerca():
    nomestore = request.args["Name"]
 #Realizzare un sito web che permetta di visualizzare tutti i dipendenti che lavorano in un certo store.
    query= f"select first_name,last_name from Sales.stores inner join Sales.staffs on Sales.stores.store_id =  Sales.staffs.store_id  where Sales.stores.store_name = '{nomestore}'  " 
    df = pd.read_sql(query, connection)
    dati = list(df.values.tolist())
    if dati == []:
        return render_template("errore.html")
    else:
     return render_template("ricerca.html",nomicolonne = df.columns.values, dati = list(df.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)

