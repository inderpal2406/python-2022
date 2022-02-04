# User need to guess a number between 1 to 100 and provide it as an input.
# The script will generate a random number and compare it with user input number.
# If both are equal, then user will get 100$. Else user won't get anything.
# Only an integer needs to be provided as input.
# If a float number, or boolean data, or unrecognized data type is provided as input then a corresponding message is displayed.
# The script will fail if a string is provided. This can be handled later using exceptions (maybe).

# Import modules.

import platform
import os
import random

# Detect the OS type and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display purpose of the script.

print(f"This script will accept a number between 1 to 100 from user.")
print(f"Then compare it with a randomly generated number between same range.")
print(f"If the numbers are equal then user would get 100$ or else nothing.\n")

# Accept the number from the user.

user_number = eval(input("Enter your guessed integer number from the range 1 to 100: "))

# Generate the random number.

random_number = random.randint(1,100)

# Compare the numbers and display the result.

if type(user_number) is float:
    print(f"You have provided a float number. Please provide an integer number only between 1 to 100.")
elif type(user_number) is int:
    if user_number < 1 or user_number > 100:
        print(f"The integer number provided is out of range. Please provide an integer between 1 to 100 only.")
    elif user_number == random_number:
        print(f"Congratulations! Your guessed number {user_number} matches the randomly generated number {random_number}.")
        print(f"You won 100$.")
    else:
        print(f"Sorry! The guessed number {user_number} doesn't match the randomly generated number {random_number}.")
        print(f"You won nothing.")
elif type(user_number) is bool:
    print(f"You have provided a boolean data type. Please provide an integer number only between 1 to 100.")
else:
    print(f"An unrecognized data input type is provided, which the script cannot process. Hence, exiting script now!")
    exit(1)
