from conftest import BaseTestCase

class TestApp(BaseTestCase):
    def test_db_connection(self):
        # test che verifica la corretta connessione al database
        cur = self.conn.cursor()
        cur.execute("SELECT 1")
        result = cur.fetchone()
        assert result[0] == 1