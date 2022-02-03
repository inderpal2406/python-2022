# This script will ask user if he wants to align the text or not and then display the text as per the choice.

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

print(f"This script will accept a string from a user. Then it'll display it at centre, left & right if user wants to align the text.\n")

# Accept string from user.

user_string = input("Enter the string text: ")

# Ask user if he wants to align the text or not.

user_choice = input("Do you want to align the text? (yes/no): ")

# Display text as per the user's choice.

if user_choice == "yes":
    # Get terminal width
    term_width = os.get_terminal_size().columns
    print(f"\nAlligned text:")
    print(f"{user_string.center(term_width)}")
    print(f"{user_string.ljust(term_width)}")
    print(f"{user_string.rjust(term_width)}")
elif user_choice == "no":
    print(f"\nUnalligned text:")
    print(f"{user_string}")
else:
    print(f"Incorrect choice entered. Please enter yes/no only. Exiting script.")
    exit(1)
