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
    return render_template('index.html', pizze=pizze, bevande=bevande, ingredienti1=ingredienti1, ingredienti2=ingredienti2, ingredienti3=ingredienti3, ingredienti4=ingredienti4, ingredienti5=ingredienti5, ingredienti6=ingredienti6, ingredienti7=ingredienti7, ingredienti8=ingredienti8)


# PAGINA /create/ - funzione create()
# Connessione al database
# INSERT dei dati della prenotazione nel database
# SELECT di pizze, bevande e ingredienti per listino in create.html

@app.route('/create/', methods=('GET', 'POST'))

def create():
    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        telefono = request.form['telefono']
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
        cur.execute('INSERT INTO cliente (nome, telefono)''VALUES (%s, %s) RETURNING idcliente',(nome, telefono))
        idcliente = cur.fetchone()[0]
        cur.execute('INSERT INTO prenotazione (data, orario, idcliente)''VALUES (%s, %s, %s) RETURNING id_prenotazione',(data, orario, idcliente))
        id_prenotazione = cur.fetchone()[0]
        if n_pezzi_p1!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p1, id_prenotazione, 1))
        if n_pezzi_p2!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p2, id_prenotazione, 2))
        if n_pezzi_p3!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p3, id_prenotazione, 3))
        if n_pezzi_p4!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p4, id_prenotazione, 4))
        if n_pezzi_p5!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p5, id_prenotazione, 5))
        if n_pezzi_p6!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p6, id_prenotazione, 6))
        if n_pezzi_p7!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p7, id_prenotazione, 7))
        if n_pezzi_p8!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p8, id_prenotazione, 8))
        if n_pezzi_b1!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b1, id_prenotazione, 1))
        if n_pezzi_b2!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b2, id_prenotazione, 2))
        if n_pezzi_b3!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b3, id_prenotazione, 3))
        if n_pezzi_b4!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b4, id_prenotazione, 4))
        if n_pezzi_b5!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b5, id_prenotazione, 5))
        if n_pezzi_b6!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b6, id_prenotazione, 6))
        if n_pezzi_b7!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b7, id_prenotazione, 7))
        if n_pezzi_b8!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b8, id_prenotazione, 8))
        if n_pezzi_b9!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b9, id_prenotazione, 9))
        if n_pezzi_b10!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b10, id_prenotazione, 10))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('order', id_prenotazione=id_prenotazione, cod_coupon=cod_coupon, **request.args))
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


# PAGINA /update/ - funzione update()
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
        cur.execute ('SELECT p.idcliente FROM prenotazione p LEFT JOIN cliente c ON p.idcliente = c.idcliente WHERE p.id_prenotazione=%s',(id_prenotazione, ))
        idcliente = cur.fetchone()[0]
        cur.execute ('UPDATE cliente SET telefono=%s WHERE idcliente=%s', (telefono, idcliente))
        cur.execute ('UPDATE prenotazione SET data=%s WHERE id_prenotazione=%s', (data, id_prenotazione))
        cur.execute ('UPDATE prenotazione SET orario=%s WHERE id_prenotazione=%s', (orario, id_prenotazione))
        cur.execute("DELETE FROM ordine_pizza WHERE id_prenotazione=%s", [id_prenotazione])
        cur.execute("DELETE FROM ordine_bevanda WHERE id_prenotazione=%s", [id_prenotazione])
        if n_pezzi_p1!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p1, id_prenotazione, 1))
        if n_pezzi_p2!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p2, id_prenotazione, 2))
        if n_pezzi_p3!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p3, id_prenotazione, 3))
        if n_pezzi_p4!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p4, id_prenotazione, 4))
        if n_pezzi_p5!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p5, id_prenotazione, 5))
        if n_pezzi_p6!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p6, id_prenotazione, 6))
        if n_pezzi_p7!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p7, id_prenotazione, 7))
        if n_pezzi_p8!="0":
            cur.execute('INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza)''VALUES (%s, %s, %s)',(n_pezzi_p8, id_prenotazione, 8))
        if n_pezzi_b1!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b1, id_prenotazione, 1))
        if n_pezzi_b2!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b2, id_prenotazione, 2))
        if n_pezzi_b3!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b3, id_prenotazione, 3))
        if n_pezzi_b4!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b4, id_prenotazione, 4))
        if n_pezzi_b5!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b5, id_prenotazione, 5))
        if n_pezzi_b6!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b6, id_prenotazione, 6))
        if n_pezzi_b7!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b7, id_prenotazione, 7))
        if n_pezzi_b8!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b8, id_prenotazione, 8))
        if n_pezzi_b9!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b9, id_prenotazione, 9))
        if n_pezzi_b10!="0":
            cur.execute('INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_bevanda)''VALUES (%s, %s, %s)',(n_pezzi_b10, id_prenotazione, 10))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('order', id_prenotazione=id_prenotazione, cod_coupon=cod_coupon, **request.args))
    else:
        cur = conn.cursor()
        cur.execute('SELECT * FROM pizza ORDER BY codice_pizza;')
        pizze = cur.fetchall()
        cur.execute('SELECT * FROM bevanda ORDER BY codice_bevanda;')
        bevande = cur.fetchall()
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
        return render_template('update.html', pizze=pizze, bevande=bevande,  ingredienti1=ingredienti1, ingredienti2=ingredienti2, ingredienti3=ingredienti3, ingredienti4=ingredienti4, ingredienti5=ingredienti5, ingredienti6=ingredienti6, ingredienti7=ingredienti7, ingredienti8=ingredienti8)


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
        cur.execute("DELETE FROM ordine_pizza WHERE id_prenotazione=%s", [id_prenotazione])
        cur.execute("DELETE FROM ordine_bevanda WHERE id_prenotazione=%s", [id_prenotazione])
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
    cod_coupon = request.args.get('cod_coupon')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute ('SELECT * FROM prenotazione p JOIN cliente c ON p.idcliente = c.idcliente WHERE p.id_prenotazione=%s',(id_prenotazione, ))
    dati = cur.fetchall()
    cur.execute ('SELECT * FROM prenotazione p JOIN ordine_pizza op ON p.id_prenotazione = op.id_prenotazione JOIN pizza ON op.codice_pizza = pizza.codice_pizza  WHERE p.id_prenotazione=%s',(id_prenotazione, ))
    pizze = cur.fetchall()
    cur.execute ('SELECT * FROM prenotazione p JOIN ordine_bevanda ob ON p.id_prenotazione = ob.id_prenotazione JOIN bevanda b ON ob.codice_bevanda = b.codice_bevanda WHERE p.id_prenotazione=%s',(id_prenotazione, ))
    bevande = cur.fetchall()
    cur.execute ('SELECT * FROM coupon WHERE codice_sconto=%s', (cod_coupon, ))
    coupons = cur.fetchall()
    cur.execute("DELETE FROM coupon WHERE codice_sconto=%s", (cod_coupon, ))
    conn.commit()
    cur.close()
    conn.close()
    return render_template('order.html', dati=dati, pizze=pizze, bevande=bevande, coupons = coupons)