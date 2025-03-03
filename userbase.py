import sqlite3
from flask import session
import werkzeug
from attributes import createkey

connection = sqlite3.connect('places.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS Users (
name TEXT NOT NULL,
login TEXT NOT NULL,
password TEXT NOT NULL,
info TEXT NOT NULL,
tg TEXT NOT NULL,
token TEXT NOT NULL
)
''')
connection.commit()


def takebytoken(token):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[5] == token:
            return user[1]
    return "-"

def takeuser(log, passw):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == log and passw == user[2]:
            return True
    return False

def takeuserapi(log, passw):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == log and passw == user[2]:
            return user[5]
    return "-"

def checkexist(usname):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == usname:
            return True
    return False


def infotake(name):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == name:
            return user[3]
    return False


def createuser(name, log, passw, tg):
    if checkexist(log) == True:
        return "Логин занят"
    else:
        #print(f'INSERT INTO Users (name, login, password, info ,tg) VALUES ({name}, {log}, {passw}, "", {tg})')
        token=createkey(log)
        cursor.execute(
            'INSERT INTO Users (name, login, password, info ,tg, token) VALUES (?, ?, ?, ?, ?, ?)',
            (name, log, passw, "", tg, token))
        connection.commit()


def dopoln(username, dopinfo):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == username:
            st = user[3] + dopinfo
            cursor.execute(f'''UPDATE Users
            SET info = ?
            WHERE login = ?;
            ''', (st, username))
            connection.commit()


def login(username, password):
    if takeuser(username, password) == True:
        return True
    else:
        return False


def only(tg):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[4] == tg:
            return False
    return True


def change_password(tg, password):
    connection = sqlite3.connect('places.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[4] == tg:
            cursor.execute(f'''UPDATE Users
            SET password = ?
            WHERE tg = ?;
            ''', (password, tg))
            connection.commit()
