from tests.conftest import BaseTestCase
import pytest
import sys
sys.path.append('~/Desktop/webapp_isa_tbd/src')
from src.app import create_logic
import os
import psycopg2
import requests
from flask import Flask, request, url_for, redirect

app=Flask(__name__)

class TestApp(BaseTestCase):
    def test_db_connection(self):
        # test che verifica la corretta connessione al database
        cur = self.conn.cursor()
        cur.execute("SELECT 1")
        result = cur.fetchone()
        assert result[0] == 1

    def test_create_logic(self):
        # test che verifica che la funzione create_logic funzioni correttamente
        data = {'data': '2022-11-02', 'orario': '13:00', 'nome': 'Mario', 'telefono': '1234567890'}
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        requests.post('http://127.0.0.1:5000/create/', data=data, headers=headers)
        create_logic()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM prenotazione p JOIN cliente c ON p.idcliente = c.idcliente WHERE c.nome=%s",('Mario', ))
        result = cur.fetchone()
        assert result[0][1] == 'Mario'

    @pytest.mark.usefixtures('client')
    def test_order(client):
        response = client.get('/order/?id_prenotazione=1&cod_coupon=abc')
        assert response.status_code == 200