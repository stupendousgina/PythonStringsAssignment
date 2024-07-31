"""

2. User Input Data Processor

Objective: The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

"""
while True:
    user_name = input("Enter your first and last name, separated by a space: e.g (first last) ").lower() 

    first_last = user_name.split(" ")
    if len(first_last) == 2:
        first, last = first_last
        if len(first) <= 1:
            print("Error: Both should be at lease 2 characters long.")
        elif len(last) <=1:
            print("Error: Both should be at lease 2 characters long.")
        else:
            print(f"User name: {first} {last} is valid.")
            break