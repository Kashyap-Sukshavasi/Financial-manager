question = input("Is this your first time using my financial manager?").lower()

if question=="no":
    answer = input("What stage are you in your financial journey?\nJust to remind you, there are 3 levels. Low Income, Middle Class, and High Income!").title()
    if answer == "Low Income":
        #All the variables listed here as well as the calculations for them.
        budget_poor = float(input("What is your budget every month?"))
        groceries_poor = 0.1 * budget_poor
        emergency_poor = 0.05 * budget_poor
        clothing_poor = 0.1 * budget_poor
        rent_poor = 0.5 * budget_poor
        savings_poor = 0.25 * budget_poor
        #All the data given above using the budget to be displayed visually below using print statements.
        print("\n\n***************************************************")
        print(f"\nYour monthly budget overall is ${budget_poor}.")
        print(f"Your monthly recommended budget for groceries is ${groceries_poor}")
        print(f"Your monthly recommended budget for emergencies is ${emergency_poor}")
        print(f"Your monthly recommended budget for clothing is ${clothing_poor}")
        print(f"Your monthly recommended budget for rent is ${rent_poor}")
        print(f"Your monthly recommended budget for savings is ${savings_poor}")
        exit()
    if answer == "Middle Class":
        #All the variables listed here as well as the calculations for them.
        budget_middle = float(input("What is your budget every month?"))
        groceries_middle = 0.15 * budget_middle
        emergency_middle = 0.05 * budget_middle
        clothing_middle = 0.15 * budget_middle
        rent_middle = 0.4 * budget_middle
        savings_middle = 0.25 * budget_middle
        #All the data given above using the budget to be displayed visually below using print statements.
        print("\n\n***************************************************")
        print(f"\nYour monthly budget overall is ${budget_middle}.")
        print(f"Your monthly recommended budget for groceries is ${groceries_middle}")
        print(f"Your monthly recommended budget for emergencies is ${emergency_middle}")
        print(f"Your monthly recommended budget for clothing is ${clothing_middle}")
        print(f"Your monthly recommended budget for rent is ${rent_middle}")
        print(f"Your monthly recommended budget for savings is ${savings_middle}")
        exit()
    if answer == "High Income":
        print('This is just a filler, future code will fix this statement.')
        #This is just a filler to not have any problems with the else code on line 38
else:
    #Main place for initial code launch Ex:Greetings, run code, etc.
    print("Welcome to the All Class Financial Manager!\nCreated by Kashyap Sukshavasi")
    print("\nThere are 3 stages to this financial manager.")
    print("\nFirstly, Low Income. This is if your monthly pay is below $1,500")
    print("\nSecond, Middle Class. This is if your monthly pay is between $3,000 and $10,000.")
    print("\nFinally, High Income. This is if your monthly pay is higher that $20,000.")
