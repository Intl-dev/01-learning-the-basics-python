#If statements

#rock, paper, scissors game

import random #this takes the library to be able to use random

options = ("rock", "paper", "scissors") #the options available

computer_choice = random.choice(options) #the computer chooses a random options between thew options available

print("Let's play rock paper scissors")

user_options = int(input("enter 1 for rock, 2 for paper, or 3 for scissors: ")) #this asks you to choose between 1, 2 or 3
user_choice = ""

if user_options == 1:        #this takes the number you chose and translates it to rock, papers or scissors to store it in user_choice
    print("You chose rock")
    user_choice = "rock"
elif user_options == 2:
    print("You chose paper")
    user_choice = "paper"
elif user_options == 3:
    print("You chose scissors")
    user_choice = "scissors"


if computer_choice == "rock" and user_choice == "rock": #these operations are the possible combinations for the computer and user of rock, paper and scissors
    print("computer: rock")
    print("you: rock")
    print("It's a draw")
if computer_choice == "paper" and user_choice == "rock":
     print("computer: paper")
     print("you: rock")
     print("you've lost")
if computer_choice == "scissors" and user_choice == "rock":
    print("computer: scissors")
    print("you: rock")
    print("you've won")

if computer_choice == "rock" and user_choice == "paper":
    print("computer: rock")
    print("you: paper")
    print("you've won")
if computer_choice == "paper" and user_choice == "paper":
    print("computer: paper")
    print("you: paper")
    print("It's a draw")
if computer_choice == "scissors" and user_choice == "paper":
    print("computer: scissors")
    print("you: paper")
    print("you've lost")

if computer_choice == "rock" and user_choice == "scissors":
    print("computer: rock")
    print("you: scissors")
    print("you've lost")
if computer_choice == "paper" and user_choice == "scissors":
    print("computer: paper")
    print("you: scissors")
    print("you've won")
if computer_choice == "scissors" and user_choice == "scissors":
    print("computer: scissors")
    print("you: scissors")
    print("It's a draw")



