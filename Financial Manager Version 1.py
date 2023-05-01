question = input("Is this your first time using my financial manager?").lower()

if question=="no":
    answer = input("What stage are you in your financial journey?\nJust to remind you, there are 3 levels. Low Income, Middle Class, and High Income!").title()
    if answer == "Low Income":
        budget_poor = float(input("What is your budget every month?"))
        groceries_poor = 0.1 * budget_poor
        emergency_poor = 0.05 * budget_poor
        clothing_poor = 0.1 * budget_poor
        rent_poor = 0.5 * budget_poor
        savings_poor = 0.25 * budget_poor
        print("\n\n***************************************************")
        print(f"\nYour monthly budget overall is ${budget_poor}.")
        print(f"Your monthly recommended budget for groceries is ${groceries_poor}")
        print(f"Your monthly recommended budget for emergencies is ${emergency_poor}")
        print(f"Your monthly recommended budget for clothing is ${clothing_poor}")
        print(f"Your monthly recommended budget for rent is ${rent_poor}")
        print(f"Your monthly recommended budget for savings is ${savings_poor}")
        exit()
    if answer == "middle class":
        
    if answer == "high income":
        
    else:
        #Main place for initial code launch Ex:Greetings, run code, etc.
        print("Welcome to the All Class Financial Manager!\nCreated by Kashyap Sukshavasi")
        print("\nThere are 3 stages to this financial manager.")
        print("\nFirstly, Low Income. This is if your monthly pay is below $1,500")
        print("\nSecond, Middle Class. This is if your monthly pay is between $3,000 and $10,000.")
        print("\nFinally, High Income. This is if your monthly pay is higher that $20,000.")
