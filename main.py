import random
import os
#xo
pl = [" "]*9
win_Fl = 0

def Place():
    global pl
    os.system('cls||clear')
    for i in range(0,8,3):
        print(pl[i],"|", pl[i+1],"|", pl[i+2])

def Pat():
    kol_kl = 0
    for i in range(9):
        if pl[i] != " ":
            kol_kl += 1
    if kol_kl == 9:
        print("Pat")
        win_Fl = 1

def Player():
    while True:
        x = int(input("Введите номер клетки: "))
        if pl[x-1] == " ":
            pl[x-1] = "x"
            break
        else:
            print('Клетка уже занята')

def Comp():
    while True:
        o = random.randint(0,8)
        if pl[o] == " ":
            pl[o] = "o"
            break

def Win(a, b, c):
    global win_Fl
    if a==b==c=='x':
        print('Player win!')
        win_Fl = 1
    elif a==b==c=='o':
        print('Comp win!')
        win_Fl = 1

while win_Fl != 1: 
    Pat()
    Place()
    Player()
    Pat()
    Comp()
    Win(pl[0], pl[1],pl[2])
    Win(pl[3], pl[4],pl[5])
    Win(pl[6], pl[7],pl[8])

    Win(pl[0], pl[3],pl[6])
    Win(pl[1], pl[4],pl[7])
    Win(pl[2], pl[5],pl[8])

    Win(pl[0], pl[4],pl[8])
    Win(pl[2], pl[4],pl[6])
    Pat()
    