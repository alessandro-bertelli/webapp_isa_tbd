import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect
from src.app import get_db_connection
from datetime import date

# test function for create() function
def test_create():
    # set test data
    test_data = {
        'nome': 'test_name',
        'telefono': '1234567890',
        'data': '2022-11-02',
        'orario': '19:20',
    }

    # create test client
    app = Flask(__name__)
    client = app.test_client()

    # test post request to create() function
    response = client.post('/create/', data=test_data)

    # check if order is stored in the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT data FROM prenotazione WHERE orario = '19:20'")
    pren = cur.fetchone()
    cur.execute("SELECT nome FROM cliente WHERE telefono = '1234567890'")
    cl = cur.fetchone()
    cur.close()
    conn.close()
    assert pren[0] == date(2022, 11, 2)
    assert cl[0] == 'test_name'

    