# This script will accept user input string. 
# Then display the string in center, left & right hand side of the screen in title format.
# This script will dynamically adjust the display of string at center, left & right hand side, as per the current terminal size.

# Import modules.

import platform
import os

# Check the OS and clear the screen as per the OS type.
# Also check the width of the current terminal (number of columns) as per the OS type.

os_name=platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")
else:
    print(f"The OS of machine is neither Windows nor Linux.")
    print(f"This script is designed for Windows and Linux OS only. Hence, exiting the script now.")
    exit()

# Display purpose of the script.

print(f"This script will accept user input string.")
print(f"Then display the string in center, left & right hand side of the screen in title format.")
print(f"In title format, the first letter of each word in the string would be capitalised.\n")

# Accept user input.

user_input_string=input("Enter the string: ")

# Convert the string to title format.

user_input_string=user_input_string.title()

# Determine the terminal width.

terminal_width=os.get_terminal_size().columns

# Display string at left hand side.

print(f"\n{user_input_string.ljust(terminal_width)}")
print(f"{user_input_string.center(terminal_width)}")
print(f"{user_input_string.rjust(terminal_width)}\n")

# Display final statement to show the end of the script.

print(f"The string is displayed at center, left & right hand side of the screen as above. That's it for now.\n")
