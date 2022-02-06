# This script will accept a number between 1 to 5 from user and display the entered number in words.
# The script will fail if a string is provided as input. The script would be enhanced later to handle this gracefully.

# Import modules.

import platform
import os

# Detect the OS type and clear the screen.

if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Linux":
    os.system("clear")

# Display the purpose of the script.

print(f"This script will display the number name of an entered number between 1 to 5.\n")

# Accept the number from the user.

num = eval(input("Enter the number between 1 to 5: "))

# Check if valid input is provided. If yes then display the number name.

if type(num) is int:
    if num > 5 or num < 1:
        print(f"Out of range number is provided. Please provide a number between 1 to 5. Exiting script now!")
        exit(1)
    else:
        # Initiate a dictionary.
        number_name_dict = {1:"one",2:"two",3:"three",4:"four",5:"five"}
        print(f"\nYou have entered the number {number_name_dict.get(num)}.\n")
elif type(num) is float:
    print(f"A float number is provided. Please provide an integer between 1 to 5. Exiting script now!")
    exit(1)
elif type(num) is bool:
    print(f"A boolean value is provided. Please provide an integer between 1 to 5. Exiting script now!")
    exit(1)
else:
    print(f"The provided input cannot be recognized as valid input. Please provide a number between 1 to 5. Exiting script now!")
    exit(1)
