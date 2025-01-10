import pandas
from sklearn.linear_model import LinearRegression
import numpy as np
from parser import dread
from score import score
from attributes import getcount
import math


def obrabotka(info,kind,town):
    sc = score(info)
    pred=list(map(str,info.split("0")))
    yl=[]
    ynaz=[]
    for i in range(len(pred)-1):
        rate=pred[i][len(pred[i])-1]
        nazv=pred[i][0:-1]
        yl.append(int(rate))
        ynaz.append(nazv)
    rate=[]
    userlist=dread()
    for i2 in ynaz:
        for i in userlist:
            if i[0]==i2:
                dll=len(i)
                vrl=[]
                for i3 in range(5,dll-1):
                    vrl.append(int(i[i3]))
                rate.append(vrl)
    x=np.array(rate).reshape([len(pred)-1,7])
    y=np.array(yl).reshape([-1,1])
    model = LinearRegression()
    model.fit(x,y)

    lplace=[]
    for i2 in range(len(userlist)):
        i=userlist[i2]
        if i[1]==kind and i[2]==town:
            dll = len(i)
            zaved=np.array(i[5:dll-1]).reshape(1,-1)
            res=model.predict(zaved)
            typepl=getcount(i[dll-1],sc)
            result=int(res[0][0].round())*typepl
            lplace.append((i2,result))
    lplace.sort(key= lambda x: x[1])
    lplace.reverse()
    lzaved=[]
    lrates=[]
    for i in range(len(lplace)):
        lzaved.append(userlist[lplace[i][0]])
        lrates.append(lplace[i][1]*10+1)
    return ((lzaved,lrates))

