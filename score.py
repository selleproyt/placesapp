from parser import taketwo
def score(info):
    pred = list(map(str, info.split("0")))
    yl = []
    ynaz = []
    pred.pop(len(pred) - 1)
    for i in range(len(pred)):
        rate = pred[i][len(pred[i]) - 1]
        nazv = pred[i][0:-1]
        yl.append(int(rate))
        ynaz.append(nazv)
    #musei,pamyatniki,vystavki,japan,italy,europe,asia,else
    l1=[0,0,0,0,0,0,0,0]
    l2=[0,0,0,0,0,0,0,0]
    for i in range(len(ynaz)):
        l=taketwo(ynaz[i])
        if l[1]=="Музей":
            l1[0]+=l[0]*yl[i]
            l2[0]+=l[0]
        if l[1]=="Пямятник":
            l1[1]+=l[0]*yl[i]
            l2[1]+=l[0]
        if l[1]=="Выставка":
            l1[2]+=l[0]*yl[i]
            l2[2]+=l[0]
        if l[1]=="Японская кухня":
            l1[3]+=l[0]*yl[i]
            l2[3]+=l[0]
        if l[1]=="Итальянская кухня":
            l1[4]+=l[0]*yl[i]
            l2[4]+=l[0]
        if l[1]=="Европейская кухня":
            l1[5]+=l[0]*yl[i]
            l2[5]+=l[0]
        if l[1]=="Азиатская кухня":
            l1[6]+=l[0]*yl[i]
            l2[6]+=l[0]
        if l[1]=="Иная кухня":
            l1[7]+=l[0]*yl[i]
            l2[7]+=l[0]
    l3=[]
    for i in range(8):
        if l2[i]==0:
            l3.append(0/10)
        else:
            l3.append(round(l1[i]/l2[i]/10,2))
    return l3
