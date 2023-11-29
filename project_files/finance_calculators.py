import math 
import random


print(""" 
      
      investment - to calculate the amount of interest you'll earn on your investment. 
      bond - to calculate the amount you'll have to pay on a home loan. 
       """)

choice = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

if choice != "investment" and choice != "bond":
    print("Error. Run again")
elif choice == "investment": 
    amount = int(input("How much would you like to deposit? "))
    interest_rate = int(input("What interest rate would you like, in %. Just the number is fine: "))
    num_years = int(input("How many years do you plan to invest for? "))
    interest = str(input("Do you want a 'compound' or 'simple' investment type? ")).lower()
    r = interest_rate/100

    if interest == "compound":
        print("You chose Compound amount")
        total_amount = amount * math.pow((1 +r), num_years)
        print(f"Your total amount would be {round(total_amount,2)}")
    elif interest == "simple":
        print("You chose simple amount")
        total_amount = amount * (1 + r*num_years)
        print(f"Your total amount would be {round(total_amount,2)}")
    else: 
        print("Error")

elif choice == "bond":
    """
○ The present value of the house. e.g. 100000
○ The interest rate. e.g. 7
○ The number of months they plan to take to repay the bond. e.g. 120
    """
    house_value = int(input("What is the present value of the house? "))
    interest_rate = int(input("What interest rate would you like, in %? "))
    months = int(input("How many months would you like to take to repay the bond? "))
    i = (interest_rate/100)/12
    repayment = (i * house_value)/(1 - (1 + i)**(-months))
    print(f"Your monthly repayments will be {round(repayment,2)}")






    








