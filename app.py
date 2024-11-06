from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Therese G in 3308"'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://goshen_db_user:lN6qAMBw37XksBf4CrF9NPlSHpw5loXf@dpg-csluhru8ii6s73b7agc0-a/goshen_db")
    conn.close()
    return 'Database connection successful'
