from flask import Flask
import sqlite3

app = Flask(__name__)

# set auto reload on code change
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run()
