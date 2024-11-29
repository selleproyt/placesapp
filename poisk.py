from parser import dread
def place(userlist):
    try:
        l=dread()
        town = userlist[0]
        count=int(userlist[1])
        atmosphere=int(userlist[2])
        price = int(userlist[3])
        color = int(userlist[4])
        type=userlist[5]
        l2=[]
        for i in range(len(l)):
            place2=l[i]
            if place2[2]==town and place2[1]==type:
                cnt=abs(atmosphere-int(place2[5]))+abs(price-int(place2[6]))+abs(color-int(place2[8]))
                l2.append((i,cnt))
        l2.sort(key=lambda x: x[1])
        l3=[]
        l4=[]
        for i in range(count):
            l4.append(l2[i][1]*25)
        for i in range(count):
            l3.append(l[l2[i][0]])
        return ((l3,l4))
    except:
        return ['error']




