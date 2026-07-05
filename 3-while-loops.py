#While loops

#ATM program

money = 1000
exit = False

while not exit: #this makes that the code inside it executes while you haven't exited the program
    option_chosen = input("Enter your option: 1. Check your money , 2. Take out money, 3. Deposit money, 4. Exit ") #this gives you the options available to choose, check money, take out money, deposit money and exit

    if option_chosen == "1": #this one is to check your money
        print(f"You have ${money} in your account")

    elif option_chosen == "2": #this one is to take out money
        money_taken = int(input("Enter amount of money to take out: "))
        if money_taken <= money:
            money = money - money_taken
            print(f"You have taken ${money_taken} of your account successfully") #if you do have enough it tells you that you have taken out the money successfully
        else: #this is a warning to tell you that you don't have enough money to take out if you want to take more than you have
            print("not enough funds int your account to take out")

    elif option_chosen == "3": #this one is to deposit money
        money_introduced = int(input("Enter your money to deposit: "))
        money = money_introduced + money
        print(f"you have successfully deposited ${money_introduced}")

    elif option_chosen == "4": #this one is to exit the program
        print("You have exited the program successfully")
        exit = True #this makes the while loop no longer work because its condition was having this False


