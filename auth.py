import sqlite3
from flask import session
import werkzeug
connection = sqlite3.connect('places.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS auth (
uscode TEXT NOT NULL,
login TEXT NOT NULL,
password TEXT NOT NULL,
name TEXT NOT NULL,
verifcode TEXT NOT NULL,
tg TEXT NOT NULL
)
''')
connection.commit()

def takecode(uscode):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM auth')
    users = cursor.fetchall()
    for user in users:
        if user[0]==uscode:
            return user[4]
    return "Неверный код"

def takeuser(uscode):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM auth')
    users = cursor.fetchall()
    for user in users:
        if user[0]==uscode:
            return [user[1],user[2],user[3],user[5]]
    return False

def createuser(uscode, name,log,passw,verifcode):
    cursor.execute(
        'INSERT INTO auth (uscode, name, login, password, verifcode, tg) VALUES (?, ?, ?, ?, ?, ?)',
        (uscode,name,log,passw,verifcode,""))
    connection.commit()


def dopoln(username,tg):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM auth')
    users = cursor.fetchall()
    for user in users:
        if user[0] == username:
            cursor.execute(f'''UPDATE auth
            SET tg = ?
            WHERE uscode = ?;
            ''',(tg,username))
            connection.commit()
