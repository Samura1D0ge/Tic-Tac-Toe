import random
import os
#xo
pl = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
win_Fl = 0

def Place():
    global pl
    os.system('cls||clear')
    for i in pl:
        print(i)

def Pat():
    kol_kl = 0
    for i in range(3):
        for j in range(3):
            if pl[i][j] != " ":
                kol_kl += 1
    if kol_kl == 9:
        print("Pat")
        win_Fl = 1

def Player():
    while True:
        x = int(input("Введите координату Х : "))
        y = int(input("Введите координату Y : "))
        if pl[x-1][y-1] == " ":
            pl[x-1][y-1] = "x"
            break
        else:
            print('Клетка уже занята')

def Comp():
    while True:
        xc = random.randint(1,3)
        yc = random.randint(1,3)
        if pl[xc-1][yc-1] == " ":
            pl[xc-1][yc-1] = "o"
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
    Win(pl[0][0],pl[0][1],pl[0][2])
    Win(pl[1][0],pl[1][1],pl[1][2])
    Win(pl[2][0],pl[2][1],pl[2][2])

    Win(pl[0][0],pl[1][0],pl[2][0])
    Win(pl[0][1],pl[1][1],pl[2][1])
    Win(pl[0][2],pl[1][2],pl[2][2])

    Win(pl[0][0],pl[1][1],pl[2][2])
    Win(pl[0][2],pl[1][1],pl[2][0])
    Pat()
    