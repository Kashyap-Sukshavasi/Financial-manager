def main_code_deposit():
    #Importing all the libraries needed for this project
    import os
    import math
    import time

    print("Welcome to my fixed deposit calculator built by Kashyap Sukshavasi!")
    question1 = input("Is this your first time using my budget manager [yes/no]?: ").title()

    if question1 == "No":
        print("\n\nThis is a fixed deposit calculator.")
        principle = float(input("What is your principle amount in your local currency?: "))
        interest = float(input("What is the interest rate for your fixed deposit.\nNote: Give the value in the numerical percentage %\nWhat is your ineterest?: "))
        time_year = float(input("What is the time for your fixed deposit in years?: "))
        i_money = principle * (interest/100) * time_year
        p_money = i_money + principle
        print(f"Your principle amount is ${principle} in your local currency.")
        print(f"Your interest rate in percentages is {interest}%.")
        print(f"Your time for the fixed deposit in years is {time_year} years.")
        print(f"The money you will get for interest is ${i_money} in your local currency.")
        print(f"Your total money including all charges ${p_money} in your local currency.")
main_code_deposit()