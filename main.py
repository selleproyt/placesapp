from flask import Flask
from flask import redirect
from poisk import place
from flask import request,session,g
from flask import render_template
from parser import dimport
from userbase import createuser,login
from captcha.image import ImageCaptcha
import random
app = Flask(__name__)
app.config['SECRET_KEY']="5a38877f6f7b7bb3fcb2c8a55027241210df24b1"
key=0



@app.route("/")
def index():
    return render_template('main.html')

@app.route("/registration")
def registration():
    global key
    image=ImageCaptcha(width=200,height=100)
    key=random.randint(1000,10000)
    data=image.generate(str(key))
    image.write(str(key),'static/img/demo.png')
    return render_template('regform.html')



@app.route("/submitreg", methods=['POST'])
def submitreg():
    username = request.form["username"]
    password = request.form["password"]
    name = request.form["name"]
    captcha=request.form["captcha"]
    if captcha==str(key):
        resultofreg=createuser(name, username, password)
        if resultofreg=="Логин занят":
            return f"Логин занят"
        else:
            return f'<meta http-equiv="refresh" content="1; url=http://192.168.102.100:5000/login">'
    else:
        return f"Неверная капча, попробуйте еще раз"



@app.route("/login")
def loginmain():
    return render_template('login.html')



@app.route("/submitlogin", methods=['POST'])
def submitlogin():
    username = request.form["username"]
    password = request.form["password"]

    if login(username,password)==True:
        session['usname'] = str(username)
        session.modified = True
        return f'<meta http-equiv="refresh" content="1; url=http://192.168.102.100:5000/user">'
    else:
        return f'<meta http-equiv="refresh" content="1; url=http://192.168.102.100:5000/registration">'


@app.route("/admin")
def admin():
    return render_template('admin.html')



@app.route("/user")
def user():
    try:
        username = session.get('usname')
        if username is not None:
            return render_template('lk.html',name=username)
        else:
            return f'<meta http-equiv="refresh" content="1; url=http://192.168.102.100:5000/login">'
    except:
        return f'<meta http-equiv="refresh" content="1; url=http://192.168.102.100:5000/login">'



@app.route("/places/<parameters>")
def places(parameters):
    #return f"Привет, {parameters}!"
    try:
        parameters=list(map(str,parameters.split("&")))
        return render_template("results.html",results=place(parameters)[0],resscore=place(parameters)[1],dlp=len(place(parameters)[0]))
    except:
        return f"Неверный формат"


@app.route('/submit', methods=['POST'])
def submitrest():
  try:
      userlist = [request.form['town'],request.form['count'],request.form['atmosphere'],request.form['price'],request.form['side']]
      s=""
      for i in range(len(userlist)):
          if i!=len(userlist)-1:
              s+=userlist[i]
              s+="&"
          else:
              s+=userlist[i]
      return f'<meta http-equiv="refresh" content="1; url=http://192.168.102.100:5000/places/{s}">'
  except:
      return render_template('error.html')

@app.route('/submitadmin', methods=['POST'])
def submitadmin():
  try:
        if request.form["password"]=="adminworld23":
            userlist = [request.form['name'],request.form['type'],request.form['town'],request.form['check'],request.form['info'],int(request.form['atmosphere']),int(request.form['price']),int(request.form['cousine']),int(request.form['side']),int(request.form['advert'])]
            dimport(userlist)

            return f'OK'
        else:
            return "error"
  except:
      return render_template('error.html')
app.run(host='192.168.102.100')