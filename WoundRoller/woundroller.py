"""
A GUI-based Hit Location Roller for DnD
Author: Me
Version: 1.0
Date: 29April2020
"""

import random
from tkinter import *
from tkinter import messagebox

def rolldice(num):        
    return random.randint(1,num)

def hitspot(num):
    spot = rolldice(num)
    if spot == 1:
        wound = "Head"
    elif spot == 2:
        wound = "Right Leg"
    elif spot == 3:
        wound = "Full Body"
    elif spot == 4:
        wound = "Right Hand"
    elif spot == 5:
        wound = "Right Arm"
    elif spot == 6:
        wound = "Left Foot"
    elif spot == 7:
        wound = "Right Foot"
    elif spot == 8:
        wound = "Left Hand"
    elif spot == 9:
        wound = "Left Arm"
    elif spot == 10:
        wound = "Stomach"
    elif spot == 11:
        wound = "Left Leg"
    else:
        wound = "Chest"
#    messagebox.showinfo("title", wound)
    return wound
    
def output(dice):
    rolly = rolls.get()
    rolly = rolly + "\nHit to the " + str(hitspot(dice))
    rolls.set(rolly)
    
def boom():
    rolls.set("Showing Here")

main = Tk()
main.title("Roll the Pain")
main.geometry('320x500')

rolls = StringVar()
rolls.set("Showing Here")
wounds = Label(main, textvariable = rolls, bg = "black", fg = "white", width = 25).pack(side=LEFT, fill=Y)

butts = Frame(main).pack(side=RIGHT, fill=Y)
buttwidth = 16
space1 = Label(butts, height = 14).pack()
rollwounds = Button(butts, width = buttwidth, text="Roll Wound Location", command = lambda: output(12)).pack()
blow = Button(butts, width = buttwidth, text = "Clear Output", command = boom).pack()

main.mainloop()
