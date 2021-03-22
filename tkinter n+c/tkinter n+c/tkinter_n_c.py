import os, time
from tkinter import *


window = Tk()
window.title('noughts and crosses')
window.geometry("500x700+150+150")

x = 1

currPlayer = "X"

def handlerAdd1(event):
    global x
    global currPlayer
    labText = lab1.cget("text")
    if labText == "-":
        lab1.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd2(event):
    global x
    global currPlayer

    labText = lab2.cget("text")
    if labText == "-":
        lab2.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd3(event):
    global x
    global currPlayer
    labText = lab3.cget("text")
    if labText == "-":
        lab3.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd4(event):
    global x
    global currPlayer
    labText = lab4.cget("text")
    if labText == "-":
        lab4.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd5(event):
    global x
    global currPlayer
    labText = lab5.cget("text")
    if labText == "-":
        lab5.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd6(event):
    global x
    global currPlayer
    labText = lab6.cget("text")
    if labText == "-":
        lab6.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd7(event):
    global x
    global currPlayer
    labText = lab7.cget("text")
    if labText == "-":
        lab7.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd8(event):
    global x
    global currPlayer
    labText = lab8.cget("text")
    if labText == "-":
        lab8.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")

def handlerAdd9(event):
    global x
    global currPlayer
    labText = lab9.cget("text")
    if labText == "-":
        lab9.config(text = currPlayer)
        if currPlayer == "X":
            currPlayer = "O"
        else:
            if currPlayer == "O":
                currPlayer = "X"
        winCheck()
    else:
        print("Invalid Move")


def winCon(direction):
    global currPlayer
    if direction == "XXX" or direction == "OOO":
        win = True
    else:
        win = False
    if win == True:
        if currPlayer == "X":
            currPlayer = "O"
        else:
            currPlayer = "X"
        labWin.config(text = currPlayer + "Wins!")
        gameRun = False

def winCheck():
    labText = lab1.cget("text")
    labText2 = lab2.cget("text")
    labText3 = lab3.cget("text")
    labText4 = lab4.cget("text")
    labText5 = lab5.cget("text")
    labText6 = lab6.cget("text")
    labText7 = lab7.cget("text")
    labText8 = lab8.cget("text")
    labText9 = lab9.cget("text")
    hor1 = labText + labText2 + labText3
    hor2 = labText4 + labText5 + labText6
    hor3 = labText7 + labText8 + labText9
    vert1 = labText + labText4 + labText7
    vert2 = labText2 + labText5 + labText8
    vert3 = labText3 + labText6 + labText9
    diagL = labText + labText5 + labText9
    diagR = labText3 + labText5 + labText7
    winCon(hor1)
    winCon(hor2)
    winCon(hor3)
    winCon(vert1)
    winCon(vert2)
    winCon(vert3)
    winCon(diagL)
    winCon(diagR)


gameRun = True

while gameRun == True:
    lab1 = Label(window, text = "-")
    lab1.config(height = 5, width = 10)
    lab1.grid(row = 1, column = 10)
    lab1.bind('<Button-1>', handlerAdd1)

    lab2 = Label(window, text = "-")
    lab2.config(height = 5, width = 10)
    lab2.grid(row = 1, column = 11)
    lab2.bind('<Button-1>', handlerAdd2)

    lab3 = Label(window, text = "-")
    lab3.config(height = 5, width = 10)
    lab3.grid(row = 1, column = 12)


    lab4 = Label(window, text = "-")
    lab4.config(height = 5, width = 10)
    lab4.grid(row = 2, column = 10)


    lab5 = Label(window, text = "-")
    lab5.config(height = 5, width = 10)
    lab5.grid(row = 2, column = 11)


    lab6 = Label(window, text = "-")
    lab6.config(height = 5, width = 10)
    lab6.grid(row = 2, column = 12)


    lab7 = Label(window, text = "-")
    lab7.config(height = 5, width = 10)
    lab7.grid(row = 3, column = 10)


    lab8 = Label(window, text = "-")
    lab8.config(height = 5, width = 10)
    lab8.grid(row = 3, column = 11)


    lab9 = Label(window, text = "-")
    lab9.config(height = 5, width = 10)
    lab9.grid(row = 3, column = 12)


    labWin = Label(window, text = "")
    labWin.place(x = 200, y = 300)

    btn1 = Button(window, text = "-")
    btn1.config(height = 5, width = 10)
    btn1.grid(row = 1, column = 1)
    btn1.bind('<Button-1>', handlerAdd1)

    btn2 = Button(window, text = "-")
    btn2.config(height = 5, width = 10)
    btn2.grid(row = 1, column = 2)
    btn2.bind('<Button-1>', handlerAdd2)

    btn3 = Button(window, text = "-")
    btn3.config(height = 5, width = 10)
    btn3.grid(row = 1, column = 3)
    btn3.bind('<Button-1>', handlerAdd3)

    btn4 = Button(window, text = "-")
    btn4.config(height = 5, width = 10)
    btn4.grid(row = 2, column = 1)
    btn4.bind('<Button-1>', handlerAdd4)

    btn5 = Button(window, text = "-")
    btn5.config(height = 5, width = 10)
    btn5.grid(row = 2, column = 2)
    btn5.bind('<Button-1>', handlerAdd5)

    btn6 = Button(window, text = "-")
    btn6.config(height = 5, width = 10)
    btn6.grid(row = 2, column = 3)
    btn6.bind('<Button-1>', handlerAdd6)

    btn7 = Button(window, text = "-")
    btn7.config(height = 5, width = 10)
    btn7.grid(row = 3, column = 1)
    btn7.bind('<Button-1>', handlerAdd7)

    btn8 = Button(window, text = "-")
    btn8.config(height = 5, width = 10)
    btn8.grid(row = 3, column = 2)
    btn8.bind('<Button-1>', handlerAdd8)

    btn9 = Button(window, text = "-")
    btn9.config(height = 5, width = 10)
    btn9.grid(row = 3, column = 3)
    btn9.bind('<Button-1>', handlerAdd9)

    window.mainloop()




