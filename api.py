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
import auth


app = Flask(__name__)
app.config['SECRET_KEY'] = "5a38877f6f7b7bb3fcb2c8a55027241210df24b1"
key = 0
url = "http://127.0.0.1:5000"






@app.route('/submitresponseapi/<parameters>')
def submitresponse(parameters):
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
def submitlogin(parameters):
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
def list(parameters):
    try:
        log = takebytoken(parameters)
        if log!="-":
            return dread()
    except:
        return "-"

@app.route("/userapi/<parameters>")
def user(parameters):
    try:
        parameters = list(map(str, parameters.split("&")))
        username = takebytoken(parameters)
        if username != "-":
            sc = score(infotake(username))
            return [infotake(username), sc]
        else:
            return '-'
    except:
        return '-'


@app.route("/places/<parameters>")
def places(parameters):
    # return f"Привет, {parameters}!"
    try:
        parameters = list(map(str, parameters.split("&")))
        # return f"Привет, {parameters}!"
        return render_template("results.html", results=place(parameters)[0], resscore=place(parameters)[1],
                               dlp=len(place(parameters)[0]))
    except:
        return render_template('error.html', error="Неверный формат")


@app.route('/submit', methods=['POST'])
def submitrest():
    try:
        userlist = [request.form.get('inputtown'), request.form['count'], request.form['atmosphere'], request.form['price'],
                    request.form['color'], request.form.get('type'),request.form.get('type2')]
        s = ""
        cnt = int(request.form['count'])
        if cnt < 1 or cnt > 20:
            return render_template('error.html', error="Неверный диапазон")
        else:
            for i in range(len(userlist)):
                if i != len(userlist) - 1:
                    s += userlist[i]
                    s += "&"
                else:
                    s += userlist[i]
            return f'<meta http-equiv="refresh" content="1; url={url}/places/{s}">'
    except:
        return render_template('error.html', error="Неверные параметры")


@app.route('/submitadmin', methods=['POST'])
def submitadmin():
    try:
        if request.form["password"] == "adminworld23":
            userlist = [request.form['name'], request.form['type'], request.form['town'], request.form['check'],
                        request.form['info'], int(request.form['atmosphere']), int(request.form['price']),
                        int(request.form['quality']), int(request.form['color']), int(request.form['esthetic']),
                        int(request.form['submark']), int(request.form['advert']), request.form['typeplace']]
            dimport(userlist)
            file = request.files['image']
            if file:
                # os.mkdir("img/uploads/"+str(file.filename))
                filename = "static/img/places/" + (file.filename)
                file.save(filename)

            return f'OK'
        else:
            return "error"
    except:
        return render_template('error.html')


@app.route('/submitfromlk/<parameters>', methods=['POST'])
def submitnetwork(parameters):
    try:
        town = request.form.get('town')
        type = request.form.get('type')
        return render_template("results.html", results=obrabotka(parameters, type, town)[0],
                               resscore=obrabotka(parameters, type, town)[1],
                               dlp=len(obrabotka(parameters, type, town)[0]))
    except:
        return render_template('error.html',
                               error="Вы оценили недостаточно мест, или в базе нет мест по вашему запросу.")


@app.route('/submitfromlk/', methods=['POST'])
def submitnetwork2():
    return render_template('error.html', error="Вы еще не оценивали места")


app.run()
