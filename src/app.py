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
        data = request.form['data']
        orario = request.form['orario']
        # n_p_p = request.form['n_p_p']
        # cod_p = request.form['cod_p']
        cod_coupon = request.form['cod_coupon']
        cur = conn.cursor()
        cur.execute('INSERT INTO cliente (nome, telefono)''VALUES (%s, %s) RETURNING idcliente',(nome, telefono))
        idcliente = cur.fetchone()[0]
        cur.execute('INSERT INTO prenotazione (data, orario, idcliente)''VALUES (%s, %s, %s) RETURNING id_prenotazione',(data, orario, idcliente))
        id_prenotazione = cur.fetchone()[0]
        # for count in range(8):
        #     if n_p_p[count]!=0:
        #         cur.execute('INSERT INTO ordine_pizza (n_pezzi, codice_pizza)''VALUES (%s, %s)',(n_p_p[count], cod_p[count]))
        #     count += 1
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('order', id_prenotazione=id_prenotazione, **request.args))
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


# PAGINA /update/ - funzione eduit()
# Connessione al database
# INSERT dei dati necessari per identificare la prenotazione nel database e aggiornarla
# SELECT di pizze, bevande e ingredienti per listino in create.html

@app.route('/update/', methods=('GET', 'POST'))

def update():
    conn = get_db_connection()
    if request.method == 'POST':
        id_prenotazione = request.form['id_prenotazione']
        telefono = request.form['telefono']
        data = request.form['data']
        orario = request.form['orario']
        cod_coupon = request.form['cod_coupon']
        cur = conn.cursor()
        cur.execute ('SELECT p.idcliente FROM prenotazione p LEFT JOIN cliente c ON p.idcliente = c.idcliente WHERE p.id_prenotazione=%s',(id_prenotazione, ))
        idcliente = cur.fetchone()[0]
        cur.execute ('UPDATE cliente SET telefono=%s WHERE idcliente=%s', (telefono, idcliente))
        cur.execute ('UPDATE prenotazione SET data=%s WHERE id_prenotazione=%s', (data, id_prenotazione))
        cur.execute ('UPDATE prenotazione SET orario=%s WHERE id_prenotazione=%s', (orario, id_prenotazione))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('order', id_prenotazione=id_prenotazione, **request.args))
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
        id_prenotazione = request.form['id_prenotazione']
        cur=conn.cursor()
        cur.execute ('SELECT p.idcliente FROM prenotazione p LEFT JOIN cliente c ON p.idcliente = c.idcliente WHERE p.id_prenotazione=%s',(id_prenotazione, ))
        idcliente = cur.fetchone()[0]
        cur.execute("DELETE FROM prenotazione WHERE id_prenotazione=%s", [id_prenotazione])
        cur.execute("DELETE FROM cliente WHERE idcliente=%s", [idcliente])
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('delete.html')


# PAGINA /order/ - funzione order()
# Connessione al database
# SELECT tutte le informazioni necessarie per il riepilogo dell'ordine.

@app.route('/order/')

def order():
    id_prenotazione = request.args.get('id_prenotazione')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute ('SELECT * FROM prenotazione p JOIN cliente c ON p.idcliente = c.idcliente WHERE p.id_prenotazione=%s',(id_prenotazione, ))
    dati = cur.fetchall()
    cur.execute ('SELECT * FROM prenotazione p JOIN ordine_pizza op ON p.id_prenotazione = op.id_prenotazione JOIN pizza ON op.codice_pizza = pizza.codice_pizza  WHERE p.id_prenotazione=%s',(id_prenotazione, ))
    pizze = cur.fetchall()
    cur.execute ('SELECT * FROM prenotazione p JOIN ordine_bevanda ob ON p.id_prenotazione = ob.id_prenotazione JOIN bevanda b ON ob.codice_bevanda = b.codice_bevanda WHERE p.id_prenotazione=%s',(id_prenotazione, ))
    bevande = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('order.html', dati=dati, pizze=pizze, bevande=bevande)