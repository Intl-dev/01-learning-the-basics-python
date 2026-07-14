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
    slow_text("'I heard you like to gamble'")
    #ytime.sleep(2.5)
    slow_text("'Do you want me to explain you how to play? (y/n)'")
    choose = input()
    if choose == "y":
        slow_text("'at your left you can see a slot machine'")
        # time.sleep(2.5)
        slow_text("'that is where you are going to get the money'")
        time.sleep(2.5)
        slow_text("'at your right there's a shelf where you can get items to get perks to get more money'")
        time.sleep(2.5)
        slow_text("'do you see that ATM?'")
        time.sleep(2.5)
        slow_text("'well it shows the amount of money you have to pay before a certain time period'")
        time.sleep(2.5)
        slow_text("'if you dont pay it the trapdoor below you will open'")
        time.sleep(2.5)
        slow_text("'I dont think you want that so G O O D  L U C K'")
        print("")
    else:
        print("")


lost = False
leave_game = False

money = 13
rounds_left = 3
spins_left = 0
debt = 75
total_money_deposited = 0
money_deposited = 0
interest = 7
spins_price_7 = 7
spins_price_3 = 3
cannot_buy_spins = False

lemon_value = 2
cherry_value = 2
clover_value = 3
bell_value = 3
diamond_value = 5
moai_value = 5
seven_value = 7

horizontal_combo_value = 1
vertical_combo_value = 1
diagonal_combo_value = 1
horizontal_l_combo_value = 2
horizontal_xl_combo_value = 3
zig_combo_value = 4
zag_combo_value = 4
up_piramid_combo_value = 7
down_piramid_combo_value = 7
eye_combo_value = 8
full_combo_value = 10

simbols = ["🍋", "🍒", "🍀", "🔔", "💎", "🗿", "7"]
lemon_chance = 20
cherry_chance = 20
clover_chance = 15
bell_chance = 15
diamond_chance = 11
moai_chance = 11
seven_chance = 8
chances = [lemon_chance, cherry_chance, clover_chance, bell_chance, diamond_chance, moai_chance, seven_chance]

def LETS_GO_GAMBLING():

    total_money_won = 0
    row_1 = []
    row_2 = []
    row_3 = []
    for i in range(5):
        row_1.append(random.choices(simbols, weights=chances, k=1)[0]) #I got the "random.choices(simbols, weights=chances, k=1)[0]" from the internet, I didn't know how to give different chances to each simbol
        row_2.append(random.choices(simbols, weights=chances, k=1)[0]) #But what it does is take a simbol from the simbols list and give it a chance to be chosen from the chances list
        row_3.append(random.choices(simbols, weights=chances, k=1)[0])

    print("")
    print(f"| {row_1[0]} | | {row_1[1]} | | {row_1[2]} | | {row_1[3]} | | {row_1[4]} |")
    print(f"| {row_2[0]} | | {row_2[1]} | | {row_2[2]} | | {row_2[3]} | | {row_2[4]} |")
    print(f"| {row_3[0]} | | {row_3[1]} | | {row_3[2]} | | {row_3[3]} | | {row_3[4]} |")


    # VERTICAL COMBOS (3 IN A ROW)


    # --- Column 1 ---
    if row_1[0] == row_2[0] and row_1[0] == row_3[0]:
        print("Vertical line of 3 in column 1")
        simbol = row_1[0]
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")

    # --- Column 2 ---
    if row_1[1] == row_2[1] and row_1[1] == row_3[1]:
        print("Vertical line of 3 in column 2")
        simbol = row_1[1]
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
            print(f"+ {(cherry_value * 3) * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")

    # --- Column 3 ---
    if row_1[2] == row_2[2] and row_1[2] == row_3[2]:
        print("Vertical line of 3 in column 3")
        simbol = row_1[2]
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
            print(f"+ {(cherry_value * 3) * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")

    # --- Column 4 ---
    if row_1[3] == row_2[3] and row_2[3] == row_3[3]:
        print("Vertical line of 3 in column 4")
        simbol = row_1[3]
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
            print(f"+ {(cherry_value * 3) * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")

    # --- Column 5 ---
    if row_1[4] == row_2[4] and row_1[4] == row_3[4]:
        print("Vertical line of 3 in column 5")
        simbol = row_1[4]
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
            print(f"+ {(cherry_value * 3) * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")


    # HORIZONTAL COMBOS (3 IN A ROW)


    # --- ROW 1 (Left, Center, Right) ---
    if row_1[0] == row_1[1] and row_1[1] == row_1[2]:
        print("Horizontal line of 3 in row 1 (Left)")
        simbol = row_1[0]
    elif row_1[1] == row_1[2] and row_1[2] == row_1[3]:
        print("Horizontal line of 3 in row 1 (Center)")
        simbol = row_1[1]
    elif row_1[2] == row_1[3] and row_1[3] == row_1[4]:
        print("Horizontal line of 3 in row 1 (Right)")
        simbol = row_1[2]
    else:
        simbol = None

    if simbol:
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
            print(f"+ {(cherry_value * 3) * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")

    # --- ROW 2 (Left, Center, Right) ---
    if row_2[0] == row_2[1] and row_2[1] == row_2[2]:
        print("Horizontal line of 3 in row 2 (Left)")
        simbol = row_2[0]
    elif row_2[1] == row_2[2] and row_2[2] == row_2[3]:
        print("Horizontal line of 3 in row 2 (Center)")
        simbol = row_2[1]
    elif row_2[2] == row_2[3] and row_2[3] == row_2[4]:
        print("Horizontal line of 3 in row 2 (Right)")
        simbol = row_2[2]
    else:
        simbol = None

    if simbol:
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
            print(f"+ {(cherry_value * 3) * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")

    # --- ROW 3 (Left, Center, Right) ---
    if row_3[0] == row_3[1] and row_3[1] == row_3[2]:
        print("Horizontal line of 3 in row 3 (Left)")
        simbol = row_3[0]
    elif row_3[1] == row_3[2] and row_3[2] == row_3[3]:
        print("Horizontal line of 3 in row 3 (Center)")
        simbol = row_3[1]
    elif row_3[2] == row_3[3] and row_3[3] == row_3[4]:
        print("Horizontal line of 3 in row 3 (Right)")
        simbol = row_3[2]
    else:
        simbol = None

    if simbol:
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * horizontal_combo_value
            print(f"+ {(lemon_value * 3) * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * horizontal_combo_value
            print(f"+ {(cherry_value * 3) * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * horizontal_combo_value
            print(f"+ {(clover_value * 3) * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * horizontal_combo_value
            print(f"+ {(bell_value * 3) * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * horizontal_combo_value
            print(f"+ {(diamond_value * 3) * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * horizontal_combo_value
            print(f"+ {(moai_value * 3) * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * horizontal_combo_value
            print(f"+ {(seven_value * 3) * horizontal_combo_value}")

    # DIAGONAL COMBOS (3 IN A ROW)

    # --- DIAGONAL DOWNWARDS ---


    if row_1[0] == row_2[1] and row_2[1] == row_3[2]:
        print("Diagonal down line of 3 (Left)")
        simbol = row_1[0]


    elif row_1[1] == row_2[2] and row_2[2] == row_3[3]:
        print("Diagonal down line of 3 (Center)")
        simbol = row_1[1]


    elif row_1[2] == row_2[3] and row_2[3] == row_3[4]:
        print("Diagonal down line of 3 (Right)")
        simbol = row_1[2]
    else:
        simbol = None


    if simbol:
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * diagonal_combo_value
            print(f"+ {(lemon_value * 3) * diagonal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * diagonal_combo_value
            print(f"+ {(cherry_value * 3) * diagonal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * diagonal_combo_value
            print(f"+ {(clover_value * 3) * diagonal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * diagonal_combo_value
            print(f"+ {(bell_value * 3) * diagonal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * diagonal_combo_value
            print(f"+ {(diamond_value * 3) * diagonal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * diagonal_combo_value
            print(f"+ {(moai_value * 3) * diagonal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * diagonal_combo_value
            print(f"+ {(seven_value * 3) * diagonal_combo_value}")

    # --- DIAGONAL UPWARDS ---


    if row_3[0] == row_2[1] and row_2[1] == row_1[2]:
        print("Diagonal up line of 3 (Left)")
        simbol = row_3[0]


    elif row_3[1] == row_2[2] and row_2[2] == row_1[3]:
        print("Diagonal up line of 3 (Center)")
        simbol = row_3[1]


    elif row_3[2] == row_2[3] and row_2[3] == row_1[4]:
        print("Diagonal up line of 3 (Right)")
        simbol = row_3[2]
    else:
        simbol = None


    if simbol:
        if simbol == "🍋":
            total_money_won += (lemon_value * 3) * diagonal_combo_value
            print(f"+ {(lemon_value * 3) * diagonal_combo_value}")
        elif simbol == "🍒":
            total_money_won += (cherry_value * 3) * diagonal_combo_value
            print(f"+ {(cherry_value * 3) * diagonal_combo_value}")
        elif simbol == "🍀":
            total_money_won += (clover_value * 3) * diagonal_combo_value
            print(f"+ {(clover_value * 3) * diagonal_combo_value}")
        elif simbol == "🔔":
            total_money_won += (bell_value * 3) * diagonal_combo_value
            print(f"+ {(bell_value * 3) * diagonal_combo_value}")
        elif simbol == "💎":
            total_money_won += (diamond_value * 3) * diagonal_combo_value
            print(f"+ {(diamond_value * 3) * diagonal_combo_value}")
        elif simbol == "🗿":
            total_money_won += (moai_value * 3) * diagonal_combo_value
            print(f"+ {(moai_value * 3) * diagonal_combo_value}")
        elif simbol == "7":
            total_money_won += (seven_value * 3) * diagonal_combo_value
            print(f"+ {(seven_value * 3) * diagonal_combo_value}")
    print(f"Total: ${total_money_won}")
    global money
    money = money + total_money_won
narrative()

while lost == False and leave_game == False:
    print(f"Money: ${money}")
    print(f"Spins left: {spins_left}")
    print("Options:")
    print("1_Use slot machine")
    print("2_Check Shelf")
    print("3_Use ATM")
    print("4_leave the game")


    option = int(input("Enter your option: "))


    if option == 1:
        if rounds_left > 0:
            spins_bought = input(f"How many spins do you want to buy? option 1. 7 spins ${spins_price_7}, option 2. 3 spins ${spins_price_3}. (enter 1 for option 1 and 2 for option 2): ")
            if spins_bought == "1":
                spins_left = spins_left + 7
                money = money - spins_price_7

            else:
                spins_left = spins_left + 3
                money = money - spins_price_3

            while spins_left > 0:
                print(f"Spins left: {spins_left}")
                spin = input("1 to spin de slot machine (you cant cancel spinning): ")
                if spin == "1":
                    LETS_GO_GAMBLING()
                    spins_left = spins_left - 1
                else:
                    LETS_GO_GAMBLING()
                    spins_left = spins_left - 1
            rounds_left = rounds_left - 1
        else:
            if money >= debt:
                print("You are in the deadline, pay the debt")
            else:
                slow_text("You dont have enough money to pay the debt and you are in the deadline")
                time.sleep(2)
                slow_text("suddenly you hear a voice...")
                time.sleep(2)
                slow_text("'Oh oh, looks like someone is broke, well good bye'")
                time.sleep(2)
                slow_text("The trapdoor below you opens...")
                time.sleep(3)
                print("You've Lost")
                lost = True



    if option == 2:
        print("Not completed yet")
        print("")

    if option == 3:
        print("")
        print(f"💀{rounds_left} Rounds left💀")
        print(f"  Debt: ${debt}")
        print(f"  Interest: %{interest}")
        print(f"  Deposited: ${total_money_deposited}")
        deposit_choice = (input("Do you want to deposit money? (y/n): "))
        if deposit_choice == "y":
                money_deposited = int(input("Enter amount to deposit: "))

                if money_deposited <= money:
                    total_money_deposited = total_money_deposited + money_deposited
                    money = money - money_deposited
                    debt = debt - money_deposited

                else:
                    print("You cannot deposit money")

        else:
            print("")

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









