import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='alessandro',
                            port=5433,
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pizza;')
    pizze = cur.fetchall()
    cur.execute('SELECT * FROM bevanda;')
    bevande = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', pizze=pizze, bevande=bevande)

@app.route('/new_pren/', methods=('GET', 'POST'))
def new_pren():
    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        id_cliente = request.form['id_cliente']
        telefono = request.form['telefono']
        data = request.form['data']
        orario = request.form['orario']
        cod_coupon = request.form['cod_coupon']
        cur = conn.cursor()
        cur.execute('INSERT INTO cliente (nome, id_cliente, telefono)''VALUES (%s, %s, %s)',(nome, id_cliente, telefono))
        cur.execute('INSERT INTO prenotazione (data, orario, id_cliente)''VALUES (%s, %s, %s)',(data, orario, id_cliente))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        cur = conn.cursor()
        cur.execute('SELECT * FROM pizza;')
        pizze = cur.fetchall()
        cur.execute('SELECT * FROM bevanda;')
        bevande = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('new_pren.html', pizze=pizze, bevande=bevande)