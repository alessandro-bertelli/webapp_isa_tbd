#attualmente non la uso
import os
import psycopg2
import pytest

@pytest.fixture(autouse=True)
def db():
    conn = psycopg2.connect(host='localhost',
                            database='alessandro',
                            port=5433,
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    cur = connection.cursor()
    cur.execute("INSERT INTO prenotazione (id_prenotazione, data, orario, idcliente) VALUES (10000, '2025-03-06', '15:30:00', 20000)")
    cur.execute("INSERT INTO cliente (nome, telefono, id_cliente) VALUES  ('Mario Rossi', '3317987239', 20000)")
    cur.execute("INSERT INTO ordine_pizza (n_pezzi, id_prenotazione, codice_pizza) VALUES (2, 10000, 3)")
    cur.execute("INSERT INTO ordine_bevanda (n_pezzi, id_prenotazione, codice_pizza) VALUES (5, 10000, 1)")
    conn.commit()
    yield conn
    cur.execute("DELETE FROM prenotazione WHERE id_prenotazione = %s", [10000])
    cur.execute("DELETE FROM cliente WHERE id_cliente = %s", [20000])
    cur.execute("DELETE FROM ordine_pizza WHERE id_prenotazione = %s", [10000])
    cur.execute("DELETE FROM ordine_bevanda WHERE id_prenotazione = %s", [10000])
    conn.commit()
    conn.close()