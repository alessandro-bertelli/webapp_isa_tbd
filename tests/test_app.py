from tests.conftest import BaseTestCase
import sys
sys.path.append('~/Desktop/webapp_isa_tbd/src')
from src.app import create

class TestApp(BaseTestCase):
    def test_db_connection(self):
        # test che verifica la corretta connessione al database
        cur = self.conn.cursor()
        cur.execute("SELECT 1")
        result = cur.fetchone()
        assert result[0] == 1

    def test_create(self):
        # creare una richiesta di prenotazione con dati di esempio
        response = self.client.post('/create', data={'nome':'Mario Rossi', 'telefono':'1234567890', 'data':'2022-12-01', 'orario':'19.00', 'n_pezzi_p1':'2', 'n_pezzi_p2':'1', 'n_pezzi_b3':'2'})

        # chiamare la funzione create()
        create()

        # verificare che la prenotazione sia stata inserita correttamente nella tabella "prenotazione"
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM prenotazione")
                prenotazione = cur.fetchone()
                assert prenotazione is not None
                assert prenotazione[1] == '2022-12-01'
                assert prenotazione[2] == '19:00'

        # verificare che i dati del cliente siano stati inseriti correttamente nella tabella "cliente"
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM cliente WHERE nome='Mario Rossi'")
                cliente = cur.fetchone()
                assert cliente is not None
                assert cliente[1] == 'Mario Rossi'
                assert cliente[2] == '1234567890'

        # verificare che gli ordini di pizza siano stati inseriti correttamente nella tabella "ordine_pizza"
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ordine_pizza WHERE id_prenotazione={}".format(prenotazione[0]))
                ordini_pizza = cur.fetchall()
                assert len(ordini_pizza) == 2
                assert ordini_pizza[0][1] == 2
                assert ordini_pizza[0][2] == 1
                assert ordini_pizza[1][1] == 1
                assert ordini_pizza[1][2] == 2

        # verificare che gli ordini di bevande siano stati inseriti correttamente nella tabella "ordine_bevanda"
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ordine_bevanda WHERE id_prenotazione={}".format(prenotazione[0]))
                ordini_bevande = cur.fetchall()
                assert len(ordini_bevande) == 1
                assert ordini_bevande[0][1] == 2
                assert ordini_bevande[0][2] == 3