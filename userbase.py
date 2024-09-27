import sqlite3
from flask import session
import werkzeug
connection = sqlite3.connect('users.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS Users (
name TEXT NOT NULL,
login TEXT NOT NULL,
password TEXT NOT NULL,
info TEXT NOT NULL
)
''')
connection.commit()

def takeuser(log,passw):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1]==log and passw==user[2]:
            return True
    return False

def checkexist(usname):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == usname:
            return True
    return False

def createuser(name,log,passw):
    if checkexist(log)==True:
        return "Логин занят"
    else:
        cursor.execute(
            'INSERT INTO Users (name, login, password, info) VALUES (?, ?, ?, ?)',
            (name,log,passw,""))
        connection.commit()

def dopoln(username,dopinfo):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == username:
            st=user[3]+", "+dopinfo
            cursor.execute(f'''UPDATE Users
            SET info = {st}
            WHERE login = {username};
            ''')
            connection.commit()
def login(username,password):
    if takeuser(username,password)==True:
        return True
    else:
        return False

