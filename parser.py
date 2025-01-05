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
quality INTEGER,
color INTEGER,
esthetic INTEGER,
submark INTEGER,
advert INTEGER,
typeplace TEXT NOT NULL
)
''')
connection.commit()

def dwrite(name1, type1, town1,cheque1,info1,atmosphere1,price1,quality1,color1,esthetic1,submark1,advert1,typeplace1):
    cursor.execute(
        'INSERT INTO Places (name, type, town,cheque,info,atmosphere,price,quality,color,esthetic,submark,advert,typeplace) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (name1, type1, town1,cheque1,info1,atmosphere1,price1,quality1,color1,esthetic1,submark1,advert1,typeplace1))
    connection.commit()


def dread():
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
    quality INTEGER,
    color INTEGER,
    esthetic INTEGER,
    submark INTEGER,
    advert INTEGER,
    typeplace TEXT NOT NULL
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
    quality=l[7]
    color=l[8]
    esthetic=l[9]
    submark=l[10]
    advert=l[11]
    typeplace=l[12]
    dwrite(name, type, town,cheque,info,atmosphere,price,quality,color,esthetic,submark,advert,typeplace)

def taketwo(name):
    placeslist = dread()
    fl = 0
    for i in range(len(placeslist)):
        if placeslist[i][0] == name:
            return [placeslist[i][10],placeslist[i][12],placeslist[i][1]]
    return []

dread()
