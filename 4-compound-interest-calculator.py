#This isn't something I haven't seen of python, but I felt like making it

#compound calculator

print("Hello, this is a compound interest calculator")
initial_amount = int(input("Enter your initial amount of money: ")) #the initial amound of money you have
interest = float(input("Enter the interest you have: ")) #the interest you have
time_in_years = int(input("Enter the amount of time in years the money has to compound: ")) #the amount of years the money has to compound
monthly_contribution = int(input("Enter the amount of monthly contribution: "))

interest_monthly = (interest / 100) / 12
time_in_months = time_in_years * 12
result = initial_amount * (1 + interest_monthly) ** time_in_months + monthly_contribution * ((1+interest_monthly) ** time_in_months -1) / interest_monthly #the compound interest formula with monthly contributions (I had to look it up on internet)

print(f"With the initial amount of ${initial_amount} In {time_in_years} years with {interest}% you will have ${round(result)}") #result