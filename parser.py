import sqlite3

connection = sqlite3.connect('places.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS Places (
name TEXT NOT NULL,
type TEXT NOT NULL,
town TEXT NOT NULL,
cheque TEXT NOT NULL,
info TEXT NOT NULL,
atmosphere INTEGER,
price INTEGER,
cuisine INTEGER,
side INTEGER,
advert INTEGER
)
''')
connection.commit()

def dwrite(name1, type1, town1,cheque1,info1,atmosphere1,price1,cuisine1,side1,advert1):
    cursor.execute(
        'INSERT INTO Places (name, type, town,cheque,info,atmosphere,price,cuisine,side,advert) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (name1, type1, town1,cheque1,info1,atmosphere1,price1,cuisine1,side1,advert1))
    connection.commit()


def dread():
    connection = sqlite3.connect('places.db')
    cursor = connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Places (
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    town TEXT NOT NULL,
    cheque TEXT NOT NULL,
    info TEXT NOT NULL,
    atmosphere INTEGER,
    price INTEGER,
    cuisine INTEGER,
    side INTEGER,
    advert INTEGER
    )
    ''')
    connection.commit()
    userlist=[]
    cursor.execute('SELECT * FROM Places')
    users = cursor.fetchall()
    for user in users:
        userlist.append(user)
    return userlist


def checkplace(town,name):
    placeslist=dread()
    fl=0
    for i in range(len(placeslist)):
        if placeslist[i][0]==name and placeslist[i][2]==town:
            fl=1
    return fl
def dimport(l):
    name=l[0]
    type=l[1]
    town=l[2]
    cheque=l[3]
    info=l[4]
    atmosphere=l[5]
    price=l[6]
    cuisine=l[7]
    inoutside=l[8]
    advert=l[9]
    dwrite(name, type, town,cheque,info,atmosphere,price,cuisine,inoutside,advert)

dread()
