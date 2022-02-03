# This script will accept user input string, then swap its case as per the user choice.
# Swapping the case means, making small letters capital and vice-versa.
# As an advanced script, the user can provide the choice as yes/no/Yes/No/YES/NO/y/Y/n/N

# Import modules.

import platform
import os

# Detect the OS type and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display purpose of the script.

print(f"This script will accept user input string.\nThen it'll ask user if he wants to swap the case for the input string.\nThen it'll swap the case as per the user choice.\n")

# Accept user input string and his choice to swap the case.

user_string = input("Enter the string: ")
user_choice = input("Do you want to swap the case: ")

# Display result as per user's choice.

if user_choice.casefold() == "yes" or user_choice.casefold() == "y":
    print(f"\nThe string after swapping the case is as below,")
    print(f"{user_string.swapcase()}")
elif user_choice.casefold() == "no" or user_choice.casefold() == "n":
    print(f"\nThe string without swapping the case is as below,")
    print(f"{user_string}")
else:
    print(f"Incorrect choice entered. Please enter the choice again as [Yes|No|yes|no|Y|N|y|n]. Exiting script.")
    exit(1)
