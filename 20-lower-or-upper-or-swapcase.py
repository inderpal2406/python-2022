# This script will accept user input string.
# Then it will convert the string to lower/upper/swapcase as per the user choice.

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

print(f"This script will accept user input string.\nThen it'll convert the string to lower/upper/swapcase as per the user's choice.\n")

# Accept user input string and choice.

user_string = input("Enter the string: ")
user_choice = input("Do you want to convert it to [lower|upper|swapcase]: ")

# Display the string as per user's choice.

if user_choice.casefold() == "lower" or user_choice.casefold() == "l":
    print(f"\nThe string after conversion to lower case is as below,\n{user_string.lower()}")
elif user_choice.casefold() == "upper" or user_choice.casefold() == "u":
    print(f"\nThe string after conversion to upper case is as below,\n{user_string.upper()}")
elif user_choice.casefold() == "swapcase" or user_choice.casefold() == "s":
    print(f"\nThe string after swapping the case is as below,\n{user_string.swapcase()}")
else:
    print(f"Incorrect choice entered. Please enter [lower|upper|swapcase|l|u|s]. Exiting the script now.")
    exit(1)
