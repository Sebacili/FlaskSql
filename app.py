from flask import Flask,render_template, request, redirect, url_for, Response
app = Flask(__name__)

#importazione 
import pandas as pd
import pymssql
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io


@app.route('/', methods=['GET'])     
def home():
    return render_template('selezione.html')


@app.route('/selezione', methods=['GET'])     
def selezione():
    scelta = request.args["scelta"]
    if scelta=="es1":
        return redirect(url_for("es1"))
    elif scelta=="es2":
        return redirect(url_for("es2"))
    elif scelta=="es3":
        return redirect(url_for("es3"))
    elif scelta=="es4":
        return redirect(url_for("es4"))


@app.route('/es1', methods=['GET'])     
def es1():
    
    # collegamento al Database   
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS', user='cilibeanu.nicolae', password='xxx123##', database='cilibeanu.nicolae')

    # Invio query al Database e ricezione informazioni
    query = 'SELECT category_name, count(*) as numero_prodotti FROM production.products inner join production.categories on categories.category_id = products.category_id group by category_name'
    global df1
    df1 = pd.read_sql(query,conn)

    # visualizzare le informazioni
    return render_template('visEs1.html', nomiColonne = df1.columns.values, dati = list(df1.values.tolist()))



@app.route('/graficoEs1', methods=['GET'])
def graficoEs1():
    #costruzione grafico
    fig, ax = plt.subplots(figsize = (6,4))
    fig.autofmt_xdate(rotation=90)
    ax.bar(df1.category_name, df1.numero_prodotti, color='g')

    #visualizzazione grafico
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')



@app.route('/es2', methods=['GET'])     
def es2():
    
    # collegamento al Database
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS', user='cilibeanu.nicolae', password='xxx123##', database='cilibeanu.nicolae')

    # Invio query al Database e ricezione informazioni
    query = 'SELECT store_name, count(*) as numero_ordini from sales.orders inner join sales.stores on stores.store_id = orders.store_id group by store_name'
    global df2
    df2 = pd.read_sql(query,conn)

    # visualizzare le informazioni
    return render_template('visEs2.html', nomiColonne = df2.columns.values, dati = list(df2.values.tolist()))


@app.route('/graficoEs2', methods=['GET'])
def graficoEs2():
    #costruzione grafico
    fig, ax = plt.subplots(figsize = (6,4))
    fig.autofmt_xdate(rotation=90)
    ax.bar(df2.store_name, df2.numero_ordini, color='g')

    #visualizzazione grafico
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')


@app.route('/es3', methods=['GET'])     
def es3():
    
    # collegamento al Database
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS', user='cilibeanu.nicolae', password='xxx123##', database='cilibeanu.nicolae')

    # Invio query al Database e ricezione informazioni
    query = 'SELECT brand_name, count(*) as numero_prodotti FROM production.products inner join production.brands on brands.brand_id = products.brand_id group by brand_name'
    global df3
    df3 = pd.read_sql(query,conn)

    # visualizzare le informazioni
    return render_template('visEs3.html', nomiColonne = df3.columns.values, dati = list(df3.values.tolist()))



@app.route('/graficoEs3', methods=['GET'])
def graficoEs3():
    #costruzione grafico
    fig = plt.figure()
    ax = plt.axes()
    cols = ['c','b','hotpink','yellow','red','brown'] 
    ax.pie(df3.numero_prodotti,colors=cols,labels=df3.brand_name)

    #visualizzazione grafico
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')


@app.route('/es4', methods=['GET'])     
def es4():
    return render_template('es4.html')


@app.route('/ricProd', methods=['GET'])     
def ricProd():
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS', user='cilibeanu.nicolae', password='xxx123##', database='cilibeanu.nicolae')

    # Invio query al Database e ricezione informazioni
    NomeProdotto = request.args['NomeProdotto']
    query = f"select * from production.products where product_name like '{NomeProdotto}%' "
    dfProdotti = pd.read_sql(query,conn)

    # visualizzare le informazioni
    return render_template('visEs4.html', nomiColonne = dfProdotti.columns.values, dati = list(dfProdotti.values.tolist()))
    
    




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
     