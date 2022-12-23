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
    cur = conn.cursor()
    cur.execute('SELECT * FROM pizza;')
    pizze = cur.fetchall()
    cur.execute('SELECT * FROM bevanda;')
    bevande = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('new_pren.html', pizze=pizze, bevande=bevande)