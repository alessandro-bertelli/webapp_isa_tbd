import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect


# Creazione di 'app'

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='alessandro',
                            port=5433,
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

#===================================================================================================


# Creazione delle pagine dell'applicazione


# PAGINA PRINCIPALE - funzione index()
# Connessione al database
# SELECT di pizze, bevande e ingredienti per listino in index.html

@app.route('/')

def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pizza;')
    pizze = cur.fetchall()
    cur.execute('SELECT * FROM bevanda;')
    bevande = cur.fetchall()
    cur.execute('SELECT * FROM ingred_pizza;')
    ingredienti = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', pizze=pizze, bevande=bevande, ingredienti=ingredienti)


# PAGINA /create/ - funzione create()
# Connessione al database
# INSERT dei dati della prenotazione nel database
# SELECT di pizze, bevande e ingredienti per listino in create.html

@app.route('/create/', methods=('GET', 'POST'))

def create():
    conn = get_db_connection()
    if request.method == 'POST':
        count = 0
        nome = request.form['nome']
        telefono = request.form['telefono']
        cod_fiscale = request.form['cod_fiscale']
        data = request.form['data']
        orario = request.form['orario']
        n_p_p = request.form['n_p_p']
        cod_p = request.form['cod_p']
        cod_coupon = request.form['cod_coupon']
        cur = conn.cursor()
        cur.execute('INSERT INTO cliente (nome, telefono, cod_fiscale)''VALUES (%s, %s, %s)',(nome, telefono, cod_fiscale))
        cur.execute('INSERT INTO prenotazione (data, orario, cod_fiscale)''VALUES (%s, %s, %s)',(data, orario, cod_fiscale))
        for count in range(8):
            if n_p_p[count]!=0:
                cur.execute('INSERT INTO ordine_pizza (n_pezzi, codice_pizza)''VALUES (%s, %s)',(n_p_p[count], cod_p[count]))
            count += 1
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
        cur.execute('SELECT * FROM ingred_pizza;')
        ingredienti = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('create.html', pizze=pizze, bevande=bevande, ingredienti=ingredienti)


# PAGINA /edit/ - funzione eduit()
# Connessione al database
# INSERT dei dati necessari per identificare la prenotazione nel database e aggiornarla
# SELECT di pizze, bevande e ingredienti per listino in create.html

@app.route('/edit/', methods=('GET', 'POST'))

def edit():
    conn = get_db_connection()
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        cur = conn.cursor()
        cur.execute('SELECT * FROM pizza;')
        pizze = cur.fetchall()
        cur.execute('SELECT * FROM bevanda;')
        bevande = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza;')
        ingredienti = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('edit.html', pizze=pizze, bevande=bevande, ingredienti=ingredienti)


# PAGINA /delete/ - funzione delete()
# Connessione al database
# INSERT dei dati necessari per identificare la prenotazione nel database ed eliminarla

@app.route('/delete/', methods=('GET', 'POST'))

def delete():
    return render_template('delete.html')