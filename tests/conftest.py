import psycopg2
from flask import Flask
from flask_testing import TestCase

class TestConfig(object):
    DATABASE_URI = "postgresql://postgres:alessandro@localhost:5433/alessandro"
    TESTING = True
    WTF_CSRF_ENABLED = False
class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config.from_object(TestConfig)
        self.conn = psycopg2.connect(app.config['DATABASE_URI'])
        return app