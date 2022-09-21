import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    print('Creating tables...')
    connection.executescript(f.read())
    print('Done.')

connection.commit()
connection.close()