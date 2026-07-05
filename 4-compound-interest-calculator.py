#This isn't something I haven't seen of python, but I felt like making it

#compound calculator

print("Hello, this is a compound interest calculator")
initial_amount = int(input("Enter your initial amount of money: "))
interest = float(input("Enter the interest you have: "))
time_in_years = int(input("Enter the amount of time in years the money has to compound: "))

result = initial_amount * (1 + (interest / 100)) ** time_in_years


print(f"With the initial amount of ${initial_amount} In {time_in_years} years with {interest}% you will have ${round(result)}")