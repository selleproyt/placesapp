from parser import dread
def place(userlist):
    try:
        l=dread()
        town = userlist[0]
        count=int(userlist[1])
        atmosphere=int(userlist[2])
        price = int(userlist[3])
        inoutside = int(userlist[4])
        l2=[]
        for i in range(len(l)):
            place2=l[i]
            if place2[2]==town:
                cnt=abs(atmosphere-int(place2[5]))+abs(price-int(place2[6]))+abs(inoutside-int(place2[8]))
                l2.append((i,cnt))
        l2.sort(key=lambda x: x[1])
        l3=[]
        for i in range(count):
            l3.append(l[l2[i][0]])
        return(l3)
    except:
        return ['error']




