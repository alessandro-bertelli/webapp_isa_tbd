from flask import Flask
from src.app import get_db_connection
from datetime import date

# funzione di test per create()
def test_create():
    # imposto i dati di test
    test_data = {
        'nome': 'test_name',
        'telefono': '1234567890',
        'data': '1111-11-11',
        'orario': '00:00'
    }

    # creo il test client
    app = Flask(__name__)
    client = app.test_client()

    # testo la richiesta post per la funzione create()
    response = client.post('/create/', data=test_data)

    # controllo se la prenotazione è stata inserita correttamente nel database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT data FROM prenotazione WHERE orario = '00:00'")
    pren = cur.fetchone()
    cur.execute("SELECT nome FROM cliente WHERE telefono = '1234567890'")
    cl = cur.fetchone()
    cur.close()
    conn.close()
    assert pren[0] == date(1111, 11, 11)
    assert cl[0] == 'test_name'

    