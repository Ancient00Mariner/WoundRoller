import random

"""
A Terminal-based Hit Location Roller for DnD
Author: Me
Date: 5Nov2019
"""

print ('Enter to roll for hit location (\'quit\' to exit)')

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
    return wound

while True:
    num = input()
    if num == "":
        print("Hit to the " + hitspot(12))
    else:
        break
