import pandas
from sklearn.linear_model import LinearRegression
import numpy as np
from parser import dread
import math


def obrabotka(info):
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
                rate.append(i[5:])
    x=np.array(rate)
    y=np.array(yl).reshape([-1,1])
    model = LinearRegression()
    model.fit(x,y)

    lplace=[]
    for i2 in range(len(userlist)):
        i=userlist[i2]
        zaved=np.array(i[5:]).reshape(1,-1)
        res=model.predict(zaved)
        result=int(res[0][0].round())
        lplace.append((i2,result))
    lplace.sort(key= lambda x: x[1])
    lplace.reverse()
    lzaved=[]
    lrates=[]
    for i in range(len(lplace)):
        lzaved.append(userlist[lplace[i][0]])
        lrates.append(lplace[i][1])
    return ((lzaved,lrates))
