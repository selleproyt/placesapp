# -*- coding: utf-8 -*-
from flask import Flask
from flask import redirect
from poisk import place
from flask import request, session, g
from flask import render_template
from parser import dimport, checkplace, dread
from userbase import createuser, login, dopoln, takeuserapi
from captcha.image import ImageCaptcha
from net import obrabotka
from userbase import infotake, takebytoken
from score import score
import random
import smtplib
from attributes import hash2
import auth


app = Flask(__name__)
app.config['SECRET_KEY'] = "5a38877f6f7b7bb3fcb2c8a55027241210df24b1"
key = 0
url = "http://127.0.0.1:5000"



@app.route('/submitregapi/<parameters>')
def submitregapi(parameters):
    try:
        parameters = str(parameters)
        parameters = parameters.split('&')
        username = parameters[0]
        password = parameters[1]
        name = parameters[2]
        uscode1 = random.randint(1000, 9999)
        vrcode = random.randint(10000, 99999)
        auth.createuser(uscode1, username, hash2(password), name, vrcode)
        return str(uscode1)
    except:
        try:
            parameters = str(parameters)
            parameters = parameters.split('&')
            uscode = parameters[0]
            verifycode = parameters[1]
            if verifycode == auth.takecode(uscode):
                resultofreg = createuser(auth.takeuser(uscode)[1], auth.takeuser(uscode)[2], auth.takeuser(uscode)[0],
                                         auth.takeuser(uscode)[3])
                if resultofreg == "Логин занят":
                    return "BUSY LOGIN"
                else:
                    return "OK"
        except:
            return "NONE"



@app.route('/submitresponseapi/<parameters>')
def submitresponseapi(parameters):
    try:
        parameters = str(parameters)
        parameters = parameters.split('&')
        town = parameters[0]
        mark = int(parameters[1])
        name = parameters[2]
        token = parameters[3]
        log= takebytoken(token)
        if int(mark) < 10 and int(mark) > 0:
            if checkplace(town, name) == 1 and log!="-":
                dopinfo = str(name) + str(mark) + "0"
                dopoln(log, dopinfo)
                return "OK"
            else:
                return "NOT EXIST"
        else:
            return "WRONG TYPE"
    except:
        return "WRONG TYPE2"


@app.route("/submitloginapi/<parameters>")
def submitloginapi(parameters):
    try:
        parameters=str(parameters)
        parameters = parameters.split('&')
        username = parameters[0]
        password = parameters[1]
        if login(username, password) == True:
            return takeuserapi(username,password)
        else:
            return "-"
    except:
        return "-"


@app.route("/listapi/<parameters>")
def listapi(parameters):
    try:
        log = takebytoken(parameters)
        if log!="-":
            return dread()
    except:
        return "-"

@app.route("/userapi/<parameters>")
def userapi(parameters):
    try:
        username = takebytoken(parameters)
        if username != "-":
            sc = score(infotake(username))
            return [infotake(username), sc]
        else:
            return '-'
    except:
        return '-+'


@app.route("/placesapi/<parameters>")
def placesapi(parameters):
    # return f"Привет, {parameters}!"
    try:
        parameters = str(parameters)
        parameters = parameters.split('&')
        # return f"Привет, {parameters}!"
        return [place(parameters)[0], place(parameters)[1],len(place(parameters)[0])]
    except:
        return '-'






@app.route('/submitfromlkapi/<parameters>')
def submitnetworkapi(parameters):
    try:
        parameters = str(parameters)
        parameters = parameters.split('&')
        town = parameters[0]
        type = parameters[1]
        parameters=parameters[2]
        return [obrabotka(parameters, type, town)[0],obrabotka(parameters, type, town)[1]]
    except:
        return "NOT MUCH PLACES"


@app.route('/submitfromlkapi/')
def submitnetwork2api():
    return "NOT SUCH PLACES"


app.run()
