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
        n_pezzi_p1 = request.form['n_pezzi_p1']
        n_pezzi_p2 = request.form['n_pezzi_p2']
        n_pezzi_p3 = request.form['n_pezzi_p3']
        n_pezzi_p4 = request.form['n_pezzi_p4']
        n_pezzi_p5 = request.form['n_pezzi_p5']
        n_pezzi_p6 = request.form['n_pezzi_p6']
        n_pezzi_p7 = request.form['n_pezzi_p7']
        n_pezzi_p8 = request.form['n_pezzi_p8']
        n_pezzi_b1 = request.form['n_pezzi_b1']
        n_pezzi_b2 = request.form['n_pezzi_b2']
        n_pezzi_b3 = request.form['n_pezzi_b3']
        n_pezzi_b4 = request.form['n_pezzi_b4']
        n_pezzi_b5 = request.form['n_pezzi_b5']
        n_pezzi_b6 = request.form['n_pezzi_b6']
        n_pezzi_b7 = request.form['n_pezzi_b7']
        n_pezzi_b8 = request.form['n_pezzi_b8']
        n_pezzi_b9 = request.form['n_pezzi_b9']
        n_pezzi_b10 = request.form['n_pezzi_b10']
        cod_coupon = request.form['cod_coupon']
        cur = conn.cursor()
        cur.execute('INSERT INTO cliente (nome, telefono, cod_fiscale)''VALUES (%s, %s, %s)',(nome, telefono, cod_fiscale))
        cur.execute('INSERT INTO prenotazione (data, orario, cod_fiscale)''VALUES (%s, %s, %s) RETURNING id_prenotazione',(data, orario, cod_fiscale))
        prenotazione_id = cur.fetchone()[0]
        if n_pezzi_p1!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p1, prenotazione_id, 1))
        if n_pezzi_p2!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p2, prenotazione_id, 2))
        if n_pezzi_p3!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p3, prenotazione_id, 3))
        if n_pezzi_p4!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p4, prenotazione_id, 4))
        if n_pezzi_p5!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p5, prenotazione_id, 5))
        if n_pezzi_p6!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p6, prenotazione_id, 6))
        if n_pezzi_p7!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p7, prenotazione_id, 7))
        if n_pezzi_p8!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p8, prenotazione_id, 8))
        if n_pezzi_b1!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b1, prenotazione_id, 1))
        if n_pezzi_b2!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b2, prenotazione_id, 2))
        if n_pezzi_b3!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b3, prenotazione_id, 3))
        if n_pezzi_b4!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b4, prenotazione_id, 4))
        if n_pezzi_b5!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b5, prenotazione_id, 5))
        if n_pezzi_b6!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b6, prenotazione_id, 6))
        if n_pezzi_b7!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b7, prenotazione_id, 7))
        if n_pezzi_b8!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b8, prenotazione_id, 8))
        if n_pezzi_b9!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b9, prenotazione_id, 9))
        if n_pezzi_b10!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b10, prenotazione_id, 10))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        cur = conn.cursor()
        cur.execute('SELECT * FROM pizza ORDER BY codice_pizza;')
        pizze = cur.fetchall()
        cur.execute('SELECT * FROM bevanda ORDER BY codice_bevanda;')
        bevande = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 1;')
        ingredienti1 = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 2;')
        ingredienti2 = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 3;')
        ingredienti3 = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 4;')
        ingredienti4 = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 5;')
        ingredienti5 = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 6;')
        ingredienti6 = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 7;')
        ingredienti7 = cur.fetchall()
        cur.execute('SELECT * FROM ingred_pizza WHERE codice_pizza = 8;')
        ingredienti8 = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('create.html', pizze=pizze, bevande=bevande, ingredienti1=ingredienti1, ingredienti2=ingredienti2, ingredienti3=ingredienti3, ingredienti4=ingredienti4, ingredienti5=ingredienti5, ingredienti6=ingredienti6, ingredienti7=ingredienti7, ingredienti8=ingredienti8)


# PAGINA /update/ - funzione eduit()
# Connessione al database
# INSERT dei dati necessari per identificare la prenotazione nel database e aggiornarla
# SELECT di pizze, bevande e ingredienti per listino in create.html

@app.route('/update/', methods=('GET', 'POST'))

def update():
    conn = get_db_connection()
    if request.method == 'POST':
        id_pren = request.form['id_pren']
        cod_fis = request.form['cod_fis']
        telefono = request.form['telefono']
        data = request.form['data']
        orario = request.form['orario']
        cod_coupon = request.form['cod_coupon']
        cur = conn.cursor()
        cur.execute ('UPDATE cliente SET telefono=%s WHERE cod_fiscale=%s', (telefono, cod_fis))
        cur.execute ('UPDATE prenotazione SET data=%s WHERE id_prenotazione=%s', (data, id_pren))
        cur.execute ('UPDATE prenotazione SET orario=%s WHERE id_prenotazione=%s', (orario, id_pren))
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
        return render_template('update.html', pizze=pizze, bevande=bevande, ingredienti=ingredienti)


# PAGINA /delete/ - funzione delete()
# Connessione al database
# INSERT dei dati necessari per identificare la prenotazione nel database ed eliminarla

@app.route('/delete/', methods=('GET', 'POST'))

def delete():
    conn = get_db_connection()
    if request.method == 'POST':
        id_pren = request.form['id_pren']
        cod_fis = request.form['cod_fis']
        cur=conn.cursor()
        cur.execute("DELETE FROM prenotazione WHERE id_prenotazione=%s", [id_pren])
        cur.execute("DELETE FROM cliente WHERE cod_fiscale=%s", [cod_fis])
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('delete.html')