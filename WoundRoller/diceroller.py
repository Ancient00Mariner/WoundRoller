import random
from tkinter import *
from tkinter import messagebox

"""
A soundboard for DnD
Author: Me
Date: 31jul2019
"""

def rolldice(num):        
    return random.randint(1,num)

def output(dice):
    rolly = rolls.get()
    rolly = rolly + "\n" + str(rolldice(dice))
    rolls.set(rolly)

def boom():
    rolls.set("Showing Here")


main = Tk()
main.title("Dice!")
main.geometry('180x500')


rolls = StringVar()
rolls.set("Showing Here")
numbers = Label(main, textvariable = rolls, bg = "black", fg = "white").pack(side=LEFT, fill=Y)

butts = Frame(main).pack(side=RIGHT, fill=Y)
buttwidth = 5
space1 = Label(butts, height=7).pack() 
dice4 = Button(butts, width = buttwidth, text="D4", command= lambda: output(4)).pack()
dice6 = Button(butts, width = buttwidth, text="D6", command= lambda: output(6)).pack()
dice8 = Button(butts, width = buttwidth, text="D8", command= lambda: output(8)).pack()
dice10 = Button(butts, width = buttwidth, text="D10", command= lambda: output(10)).pack()
dice12 = Button(butts, width = buttwidth, text="D12", command= lambda: output(12)).pack()
dice20 = Button(butts, width = buttwidth, text="D20", command= lambda: output(20)).pack()
dice100 = Button(butts, width = buttwidth, text="D100", command= lambda: output(100)).pack()

blow = Button(butts, text="Blow it up", command=boom).pack()
"""boom = Button(butts, text="BOOM", command=main.destroy).pack()"""

main.mainloop()
