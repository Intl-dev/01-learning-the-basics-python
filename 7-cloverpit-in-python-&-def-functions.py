#CloverPit in python and def functions
import random
import time

import sys

def slow_text(text, speed=0.04): #I'm not gonna lie, I got this from the internet

    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print("")

def narrative():
    slow_text("You are taken to a room")
    #time.sleep(2.5)
    slow_text("You see a slot machine, a shelf with weird items and an ATM")
    #time.sleep(2.5)
    slow_text("Below your feet you see a trapdoor")
    #time.sleep(2.5)
    slow_text("Suddenly you hear a voice")
    #time.sleep(2)
    slow_text("'Hello player'")
    #time.sleep(2)
    slow_text("'you were taken here to pay your debt'")
    #time.sleep(2.5)
    slow_text("'at your left you can see a slot machine'")
    #time.sleep(2.5)
    slow_text("'that is where you are going to get the money'")
    #time.sleep(2.5)
    slow_text("'at your right there's a shelf where you can get items to get perks to get more money'")
    #time.sleep(2.5)
    slow_text("'do you see that ATM?'")
    #time.sleep(2.5)
    slow_text("'well it shows the amount of money you have to pay before a certain time period'")
    #time.sleep(2.5)
    slow_text("'if you dont pay it the trapdoor below you will open'")
    #time.sleep(2.5)
    slow_text("'I dont think you want that so G O O D  L U C K'")

lost = False
leave_game = False

narrative()

while lost == False and leave_game == False:
    print("Options:")
    print("1_Use slot machine")
    print("2_Check Shelf")
    print("3_Use ATM")
    print("4_leave the game")


    option = int(input("Enter your option: "))

    if option == 1:
        print("Not completed yet")
        print("")

    if option == 2:
        print("Not completed yet")
        print("")

    if option == 3:
        print("Not completed yet")
        print("")

    if option == 4:
        sure = input("Are you sure you want to leave the game? (y/n): ")
        if sure == "y":
            leave_game = True
        elif sure == "n":
            leave_game = False
            print("")
        else:
            sure = input("Invalid option, write 'y' to leave the game or 'n' to keep playing: ")
            print("")







