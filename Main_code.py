#Importing all the modules necessary to create a user interface with all the managers
import os
import time
import math
from Budget_manager  import main_code_budget
from Fixed_deposit import main_code_deposit

print("Welcome!")
print("\nThis is the Money Manager Application built for you. This app is brought to you by Kashyap Sukshavasi(Lead Programmer) and Zaid Soboh(Lead Programmer)!")
tutorial_question = input("\n\nIs this your first time using our application [yes/no]?:").title()

if tutorial_question == "Yes":
    print("\n\n********************************************")
    time.sleep(2)
    print("Loading tutorial...25%")
    time.sleep(4)
    print("Loading tutorial...75%")
    time.sleep(1)
    print("Loading tutorial...100%")
    time.sleep(2)
    print("Welcome to your tutorial!")
    print("\n\n")
elif tutorial_question == "No":
    print("\n\nYou have multiple modes to choose from, such as...")
    print("\n1 - Monthly Budget Manager")
    print("\n2 - Fixed Deposit Calculator")
    print("\n3 - Future Stuff...")
    print("\n\n")
    time.sleep(3)
    modes_question = input("Which mode would you like to use today?\nUse the numbers associated with the mode as an answer!\nYour answer:")
    if modes_question == "1":
        main_code_budget()
    if modes_question == "2":
        main_code_deposit()
