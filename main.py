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
    flp = 0
    while flp != 1:
        x = int(input("Введите координату Х : "))
        y = int(input("Введите координату Y : "))

        for i in range(3):
            for j in range(3):
                if i + 1 == x and j + 1 == y:
                    if pl[i][j] == " ":
                        pl[i][j] = "x"
                        flp = 1
                    else:
                        print("Клетка уже занята, введите другие координвты")

def Comp():
    fl = 0
    while fl != 1:
        xc = random.randint(1,3)
        yc = random.randint(1,3)
        for i in range(3):
            for j in range(3):
                if i + 1 == xc and j + 1 == yc:
                    if pl[i][j] == " ":
                        pl[i][j] = "o"
                        fl = 1
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
    