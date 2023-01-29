export FLASK_APP=app 
export FLASK_DEBUG=true
export DB_USERNAME="postgres"
export DB_PASSWORD="alessandro"

pytest tests/test_create.py
pytest tests/test_app.py