from flask import Flask
from flask import redirect
from poisk import place
from flask import request, session, g
from flask import render_template
from parser import dimport, checkplace, dread
from userbase import createuser, login, dopoln
from captcha.image import ImageCaptcha
from net import obrabotka
from userbase import infotake
from score import score
from attributes import hash2
import random
import smtplib
import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = "5a38877f6f7b7bb3fcb2c8a55027241210df24b1"
key = 0
url = "http://127.0.0.1:5000"


@app.route("/")
def index():
    return render_template('main.html')


@app.route("/registration")
def registration():
    global key
    image = ImageCaptcha(width=200, height=100)
    key = random.randint(1000, 10000)
    data = image.generate(str(key))
    image.write(str(key), 'static/img/demo.png')
    return render_template('regform.html')


@app.route("/submitresponse", methods=['POST'])
def submitresponse():
    try:
        town = request.form.get("inputtown")
        mark = request.form["mark"]
        name = request.form["name"]
        if int(mark) < 10 and int(mark) > 0:
            if checkplace(town, name) == 1:
                dopinfo = str(name) + str(mark) + "0"
                dopoln(session['usname'], dopinfo)
                return f'<meta http-equiv="refresh" content="1; url={url}/user">'
            else:
                return render_template('error.html', error="Заведения не существует")
        else:
            return render_template('error.html', error="Неверный формат оценки")
    except:
        return render_template('error.html', error="Неверный формат")


@app.route("/submitreg", methods=['POST'])
def submitreg():
    try:
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        captcha = request.form["captcha"]
        if captcha == str(key):
            uscode1 = random.randint(1000, 9999)
            vrcode = random.randint(10000, 99999)
            auth.createuser(uscode1, username, hash2(password), name, vrcode)
            return render_template('verifyform.html', code=str(uscode1))
        else:
            return render_template('error.html', error="Неверная капча, попробуйте еще раз")
    except:
        try:
            uscode = request.form["vscode"]
            verifycode = request.form["verifcode"]
            if verifycode == auth.takecode(uscode):
                resultofreg = createuser(auth.takeuser(uscode)[1], auth.takeuser(uscode)[2], auth.takeuser(uscode)[0],
                                         auth.takeuser(uscode)[3])
                if resultofreg == "Логин занят":
                    return render_template('error.html', error="Логин занят")
                else:
                    return f'<meta http-equiv="refresh" content="1; url={url}/login">'
        except:
            return render_template('error.html', error="Ничего не передано")


@app.route("/login")
def loginmain():
    return render_template('login.html')

@app.route("/premium")
def premium():
    return render_template('premium.html')

@app.route("/logout", methods=['POST'])
def logout():
    session.pop('usname')
    return f'<meta http-equiv="refresh" content="1; url={url}">'


@app.route("/submitlogin", methods=['POST'])
def submitlogin():
    username = request.form["username"]
    password = request.form["password"]

    if login(username, password) == True:
        session['usname'] = str(username)
        session.modified = True
        return f'<meta http-equiv="refresh" content="1; url={url}/user">'
    else:
        return f'<meta http-equiv="refresh" content="1; url={url}/registration">'


@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/list")
def list():
    li=dread()
    return render_template("list.html",li=li)

@app.route("/user")
def user():
    try:
        username = session.get('usname')
        if username is not None:
            sc = score(infotake(username))
            return render_template('lk.html', name=username, info=infotake(username), params=sc)
        else:
            return f'<meta http-equiv="refresh" content="1; url={url}/login">'
    except:
        return f'<meta http-equiv="refresh" content="1; url={url}/login">'


@app.route("/places/<parameters>")
def places(parameters):
    # return f"Привет, {parameters}!"
    try:
        parameters = str(parameters)
        parameters = parameters.split('&')
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
