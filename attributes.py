from random import choice
from string import ascii_letters
def nol(znach, mn):
    if znach == 0.0:
        return mn / 2
    else:
        return znach


def getcount(zn, l):
    mn = 1
    for i in range(len(l)):
        if l[i] > 0 and l[i] < mn:
            mn = l[i]
    if zn == "Музей":
        return nol(l[0], mn)
    if zn == "Памятник":
        return nol(l[1], mn)
    if zn == "Выставка":
        return nol(l[2], mn)
    if zn == "Японская кухня":
        return nol(l[3], mn)
    if zn == "Итальянская кухня":
        return nol(l[4], mn)
    if zn == "Европейская кухня":
        return nol(l[5], mn)
    if zn == "Азиатская кухня":
        return nol(l[6], mn)
    if zn == "Иная кухня":
        return nol(l[7], mn)
def createkey(username):
    username+="0key"
    username+=''.join(choice(ascii_letters) for i in range(12))
    return username
