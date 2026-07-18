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
    #time.sleep(2.5)
    slow_text("'Do you want me to explain you how to play? (y/n)'")
    choose = input()
    if choose == "y":
        slow_text("'at your left you can see a slot machine'")
        time.sleep(2.5)
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
tickets = 1
rounds_left = 3
spins_left = 0
deadline = 1
debt = 75
total_money_deposited = 30
money_deposited = 0
interest = 7
spins_price_7 = 7
spins_price_3 = 3
cannot_buy_spins = False
rounds_counter = 0

lemon_value = 2 * 3 #these are buffed because I haven't made the items yet
cherry_value = 2 * 3
clover_value = 3 * 3
bell_value = 3 * 3
diamond_value = 5 * 3
moai_value = 5 * 3
seven_value = 7 * 3

 #items
items = {
    "lemon_photo": {
        "name": "lemon_photo",
        "price": 2,
        "description": "increases the chances of lemons",
        "active": False
    },
    "cherry_photo": {
        "name": "cherry_photo",
        "price": 2,
        "description": "increases the chances of cherrys",
        "active": False
    },
    "clover_photo": {
        "name": "clover_photo",
        "price": 3,
        "description": "increases the chances of clovers",
        "active": False
    },
    "bell_photo": {
        "name": "bell_photo",
        "price": 3,
        "description": "increases the chances of bells",
        "active": False
    },
    "diamond_photo": {
        "name": "diamond_photo",
        "price": 4,
        "description": "increases the chances of diamonds",
        "active": False
    },
    "moai_photo": {
        "name": "moai_photo",
        "price": 4,
        "description": "increases the chances of moais",
        "active": False
    },
    "seven_photo": {
        "name": "seven_photo",
        "price": 5,
        "description": "increases the chances of sevens",
        "active": False
    },

}
stock = random.sample(list(items.keys()), k=3)

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
lemon_chance = 19.4
cherry_chance = 19.4
clover_chance = 14.9
bell_chance = 14.9
diamond_chance = 11.9
moai_chance = 11.9
seven_chance = 7.5
chances = [lemon_chance, cherry_chance, clover_chance, bell_chance, diamond_chance, moai_chance, seven_chance]

def show_chances(chances_available):
    weights_addition = sum(chances_available)

    for i in range(len(simbols)):
        icon = simbols[i]
        simbol_weight = chances[i]
        real_percentage = (simbol_weight / weights_addition) * 100
        print(f"{icon} : {real_percentage:.1f}%")

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
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

    # --- Column 2 ---
    if row_1[1] == row_2[1] and row_1[1] == row_3[1]:
        print("Vertical line of 3 in column 2")
        simbol = row_1[1]
        if simbol == "🍋":
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

    # --- Column 3 ---
    if row_1[2] == row_2[2] and row_1[2] == row_3[2]:
        print("Vertical line of 3 in column 3")
        simbol = row_1[2]
        if simbol == "🍋":
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

    # --- Column 4 ---
    if row_1[3] == row_2[3] and row_2[3] == row_3[3]:
        print("Vertical line of 3 in column 4")
        simbol = row_1[3]
        if simbol == "🍋":
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

    # --- Column 5 ---
    if row_1[4] == row_2[4] and row_1[4] == row_3[4]:
        print("Vertical line of 3 in column 5")
        simbol = row_1[4]
        if simbol == "🍋":
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

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
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

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
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

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
            total_money_won += lemon_value * horizontal_combo_value
            print(f"+ {lemon_value * horizontal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * horizontal_combo_value
            print(f"+ {cherry_value * horizontal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * horizontal_combo_value
            print(f"+ {clover_value * horizontal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * horizontal_combo_value
            print(f"+ {bell_value * horizontal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * horizontal_combo_value
            print(f"+ {diamond_value * horizontal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * horizontal_combo_value
            print(f"+ {moai_value * horizontal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * horizontal_combo_value
            print(f"+ {seven_value * horizontal_combo_value}")

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
            total_money_won += lemon_value * diagonal_combo_value
            print(f"+ {lemon_value * diagonal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * diagonal_combo_value
            print(f"+ {cherry_value * diagonal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * diagonal_combo_value
            print(f"+ {clover_value * diagonal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * diagonal_combo_value
            print(f"+ {bell_value * diagonal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * diagonal_combo_value
            print(f"+ {diamond_value * diagonal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * diagonal_combo_value
            print(f"+ {moai_value * diagonal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * diagonal_combo_value
            print(f"+ {seven_value * diagonal_combo_value}")

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
            total_money_won += lemon_value * diagonal_combo_value
            print(f"+ {lemon_value * diagonal_combo_value}")
        elif simbol == "🍒":
            total_money_won += cherry_value * diagonal_combo_value
            print(f"+ {cherry_value * diagonal_combo_value}")
        elif simbol == "🍀":
            total_money_won += clover_value * diagonal_combo_value
            print(f"+ {clover_value * diagonal_combo_value}")
        elif simbol == "🔔":
            total_money_won += bell_value * diagonal_combo_value
            print(f"+ {bell_value * diagonal_combo_value}")
        elif simbol == "💎":
            total_money_won += diamond_value * diagonal_combo_value
            print(f"+ {diamond_value * diagonal_combo_value}")
        elif simbol == "🗿":
            total_money_won += moai_value * diagonal_combo_value
            print(f"+ {moai_value * diagonal_combo_value}")
        elif simbol == "7":
            total_money_won += seven_value * diagonal_combo_value
            print(f"+ {seven_value * diagonal_combo_value}")

    print(f"Total: ${total_money_won}")
    global money
    money = money + total_money_won


narrative()

while lost == False and leave_game == False:
    print(f"Money: ${money}")
    print(f"Clover tickets: {tickets}")
    print(f"Spins left: {spins_left}")
    print("Options:")
    print("1_Use slot machine")
    print("2_Check Shelf")
    print("3_Use ATM")
    print("4_leave the game")

    option = int(input("Enter your option: "))
    if option == 1:
        if rounds_left > 0:
            chances = [lemon_chance, cherry_chance, clover_chance, bell_chance, diamond_chance, moai_chance, seven_chance]
            if items["lemon_photo"]["active"] == True:
                chances[0] = chances[0] * 2
            if items["cherry_photo"]["active"] == True:
                chances[1] = chances[1] * 2
            if items["clover_photo"]["active"] == True:
                chances[2] = chances[2] * 2
            if items["bell_photo"]["active"] == True:
                chances[3] = chances[3] * 2
            if items["diamond_photo"]["active"] == True:
                chances[4] = chances[4] * 2
            if items["moai_photo"]["active"] == True:
                chances[5] = chances[5] * 2
            if items["seven_photo"]["active"] == True:
                chances[6] = chances[6] * 2

            show_chances(chances)
            spins_bought = input(f"How many spins do you want to buy? option 1. 7 spins ${spins_price_7} and + 1 ticket, option 2. 3 spins ${spins_price_3} and + 2 tickets. (enter 1 for option 1 and 2 for option 2): ")
            if spins_bought == "1":
                spins_left = spins_left + 7
                tickets = tickets + 1
                money = money - spins_price_7

            else:
                spins_left = spins_left + 3
                money = money - spins_price_3
                tickets = tickets + 2

            while spins_left > 0:
                print(f"Spins left: {spins_left}")
                spin = input("1 to spin de slot machine (you cant cancel spinning): ")
                if spin == "1":
                    LETS_GO_GAMBLING()
                    spins_left = spins_left - 1
                else:
                    LETS_GO_GAMBLING()
                    spins_left = spins_left - 1
            rounds_counter = rounds_counter + 1
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
        print("")
        print(" Items Shop ")
        print(stock[0])
        print(stock[1])
        print(stock[2])
        check_option = input(f"Which item would you like to check? 1 for {stock[0]}, 2 for {stock[1]}, 3 for {stock[2]}: ")
        if check_option == "1":
            print(items[stock[0]]["name"])
            print(items[stock[0]]["description"])
            print(items[stock[0]]["price"])
            buy_item_option = input(f"Want to buy {items[stock[0]]['name']}? (y/n): ")
            if buy_item_option == "y":
                if items[stock[0]]["active"] == False:
                    if tickets >= items[stock[0]]['price']:
                        items[stock[0]]["active"] = True
                        tickets = tickets - items[stock[0]]["price"]
                        print(f"you have purchased {items[stock[0]]['name']} for {items[stock[0]]['price']} tickets")
                    else:
                        print("Not enough tickets")
                else:
                    print("You already have this item")
            else:
                print("Canceled purchase")
        elif check_option == "2":
            print(items[stock[1]]["name"])
            print(items[stock[1]]["description"])
            print(items[stock[1]]["price"])
            buy_item_option = input(f"Want to buy {items[stock[1]]['name']}? (y/n): ")
            if buy_item_option == "y":
                if items[stock[1]]["active"] == False:
                    if tickets >= items[stock[1]]['price']:
                        items[stock[1]]["active"] = True
                        tickets = tickets - items[stock[1]]["price"]
                        print(f"you have purchased {items[stock[1]]['name']} for {items[stock[1]]['price']} tickets")
                    else:
                        print("Not enough tickets")
                else:
                    print("You already have this item")
            else:
                print("Canceled purchase")
        elif check_option == "3":
            print(items[stock[2]]["name"])
            print(items[stock[2]]["description"])
            print(items[stock[2]]["price"])
            buy_item_option = input(f"Want to buy {items[stock[2]]['name']}? (y/n): ")
            if buy_item_option == "y":
                if items[stock[2]]["active"] == False:
                    if tickets >= items[stock[2]]['price']:
                        items[stock[2]]["active"] = True
                        tickets = tickets - items[stock[2]]["price"]
                        print(f"you have purchased {items[stock[2]]['name']} for {items[stock[2]]['price']} tickets")
                    else:
                        print("Not enough tickets")
                else:
                    print("You already have this item")
            else:
                print("Canceled purchase")
        else:
            print("Invalid option")
    print("")

    if option == 3:
        print("")
        print(f"💀{rounds_left} Rounds left💀")
        print(f"  Debt: ${debt}")
        print(f"  Interest: %{interest}")
        print(f"  Deposited: ${total_money_deposited}")
        atm_choice = (input("1 to deposit money, 2 to claim interests, and 3 to leave the ATM: "))
        if atm_choice == "1":
                money_deposited = int(input("Enter amount to deposit (you can put a higher number than needed if you are lazy to put the exact number, the ATM will take the exact money needed): "))
                if money_deposited <= money:
                    if money_deposited <= debt:
                        total_money_deposited = total_money_deposited + money_deposited
                        money = money - money_deposited
                        debt = debt - money_deposited
                        if debt == 0:
                            if deadline == 1:
                                print("Items shop restocked")
                                print("Congratulations, how about another deadline?")
                                debt = 200
                                deadline = deadline + 1
                                rounds_left = 3
                                stock = random.sample(list(items.keys()), k=3)
                            elif deadline == 2:
                                print("Items shop restocked")
                                print("Congratulations, how about another deadline?")
                                debt = 666
                                deadline = deadline + 1
                                rounds_left = 3
                                stock = random.sample(list(items.keys()), k=3)
                            elif deadline == 3:
                                print("Items shop restocked")
                                print("Congratulations, how about another deadline?")
                                debt = 1250
                                deadline = deadline + 1
                                rounds_left = 3
                                stock = random.sample(list(items.keys()), k=3)
                            elif deadline == 4:
                                print("Items shop restocked")
                                print("Congratulations, how about another deadline?")
                                debt = 33333
                                deadline = deadline + 1
                                rounds_left = 3
                                stock = random.sample(list(items.keys()), k=3)
                            else:
                                scaling_debt = 33333 * (3 ** (deadline - 4))
                                print("Items shop restocked")
                                print("Congratulations, how about another deadline?")
                                deadline = deadline + 1
                                rounds_left = 3
                                debt =  scaling_debt
                                stock = random.sample(list(items.keys()), k=3)
                    else:
                        money_deposited = debt
                        debt = debt - money_deposited
                        money = money - money_deposited
                        if deadline == 1:
                            print("Congratulations, how about another deadline?")
                            debt = 200
                            deadline = deadline + 1
                            rounds_left = 3
                        elif deadline == 2:
                            print("Congratulations, how about another deadline?")
                            debt = 666
                            deadline = deadline + 1
                            rounds_left = 3
                        elif deadline == 3:
                            print("Congratulations, how about another deadline?")
                            debt = 1250
                            deadline = deadline + 1
                            rounds_left = 3
                        elif deadline == 4:
                            print("Congratulations, how about another deadline?")
                            debt = 33333
                            deadline = deadline + 1
                            rounds_left = 3
                        else:
                            scaling_debt = 33333 * (3 ** (deadline - 4))
                            print("Congratulations, how about another deadline?")
                            deadline = deadline + 1
                            debt = scaling_debt
                        


                else:
                    print("You cannot deposit money")
        elif atm_choice == "2":
            total_interests =  (total_money_deposited * (interest * 0.01)) * rounds_counter
            print(f"Total interests claimed:  ${round(total_interests)}")
            money = money + round(total_interests)
            total_interests = 0
            rounds_counter = 0
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









