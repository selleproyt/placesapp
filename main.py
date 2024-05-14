from flask import Flask
from poisk import place
from flask import request
from flask import render_template
from parser import dimport

app = Flask(__name__)
app.config['SECRET_KEY']="5a38877f6f7b7bb3fcb2c8a55027241210df24b1"

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')


@app.route("/lk")
def admin():
    return render_template('lk.html')


@app.route("/places/<parameters>")
def places(parameters):
    #return f"Привет, {parameters}!"
    try:
        parameters=list(map(str,parameters.split("&")))
        return place(parameters)
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

      return f'<meta http-equiv="refresh" content="1; url=http://localhost:5000/places/{s}">'
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
app.run()