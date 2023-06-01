import flask
import psycopg2

app = flask.Flask(__name__)

app.secret_key = "super secret key"

# set your own database name, user name and password
db = "dbname='movieProject' user='postgres' host='localhost' password='ordrup'" #potentially wrong password
conn = psycopg2.connect(db)
