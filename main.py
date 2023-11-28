import random
import sys
#xo
pl = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
win_Fl = 0

def Place():
    global pl
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

def Win():
    global win_Fl
    # for player
    if pl[0][0] == pl[0][1] ==  pl[0][2] == 'x':
        print("Player win!")
        win_Fl = 1
    if pl[1][0] == pl[1][1] ==  pl[1][2] == 'x':
        print("Player win!")
        win_Fl = 1
    if pl[2][0] == pl[2][1] ==  pl[2][2] == 'x':
        print("Player win!")
        win_Fl = 1

    if pl[0][0] == pl[1][0] ==  pl[2][0] == 'x':
        print("Player win!")
        win_Fl = 1
    if pl[0][1] == pl[1][1] ==  pl[2][1] == 'x':
        print("Player win!")
        win_Fl = 1
    if pl[0][2] == pl[1][2] ==  pl[2][2] == 'x':
        print("Player win!")
        win_Fl = 1

    if pl[0][0] == pl[1][1] ==  pl[2][2] == 'x':
        print("Player win!")
        win_Fl = 1
    if pl[0][2] == pl[1][1] ==  pl[2][0] == 'x':
        print("Player win!")
        win_Fl = 1

    #for computer
    if pl[0][0] == pl[0][1] ==  pl[0][2] == 'o':
        print("Comp win!")
        win_Fl = 1
    if pl[1][0] == pl[1][1] ==  pl[1][2] == 'o':
        print("Comp win!")
        win_Fl = 1
    if pl[2][0] == pl[2][1] ==  pl[2][2] == 'o':
        print("Comp win!")
        win_Fl = 1

    if pl[0][0] == pl[1][0] ==  pl[2][0] == 'o':
        print("Comp win!")
        win_Fl = 1
    if pl[0][1] == pl[1][1] ==  pl[2][1] == 'o':
        print("Comp win!")
        win_Fl = 1
    if pl[0][2] == pl[1][2] ==  pl[2][2] == 'o':
        print("Comp win!")
        win_Fl = 1

    if pl[0][0] == pl[1][1] ==  pl[2][2] == 'o':
        print("Comp win!")
        win_Fl = 1
    if pl[0][2] == pl[1][1] ==  pl[2][0] == 'o':
        print("Comp win!")
        win_Fl = 1

while win_Fl != 1:
    Pat()
    Player()
    Pat()
    Comp()
    Place()
    Pat()
    Win()