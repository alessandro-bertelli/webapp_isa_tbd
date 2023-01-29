# imposto le variabili globali per la connessione con il database postgres
# e per l'esecuzione dei test pytest
export FLASK_APP=app 
export FLASK_DEBUG=true
export DB_USERNAME="postgres"
export DB_PASSWORD="alessandro"

pytest test_create.py
pytest test_app.py