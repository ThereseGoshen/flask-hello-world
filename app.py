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

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgresql://goshen_db_user:lN6qAMBw37XksBf4CrF9NPlSHpw5loXf@dpg-csluhru8ii6s73b7agc0-a/goshen_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return 'Table created'

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgresql://goshen_db_user:lN6qAMBw37XksBf4CrF9NPlSHpw5loXf@dpg-csluhru8ii6s73b7agc0-a/goshen_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),   
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Therese', 'Goshen', 'CU Boulder', 'Buffs', 3308);
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Populated'

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgresql://goshen_db_user:lN6qAMBw37XksBf4CrF9NPlSHpw5loXf@dpg-csluhru8ii6s73b7agc0-a/goshen_db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball')
    records = cur.fetchall()
    conn.close()
    response_str = ''
    response_str += '<table>'
    for player in records:
        response_str += '<tr>'
        for info in player:
            response_str += '<td>{}</td>'.format(info)
        response_str += '</tr>'
    response_str += '</table>'
    return response_str

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgresql://goshen_db_user:lN6qAMBw37XksBf4CrF9NPlSHpw5loXf@dpg-csluhru8ii6s73b7agc0-a/goshen_db")
    cur = conn.cursor()
    cur.execute('''DROP TABLE Basketball''')
    conn.commit()
    conn.close()
    return 'Table dropped'