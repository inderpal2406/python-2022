# This script will accept user input string. 
# Then display the string in center, left & right hand side of the screen in title format.

# Import modules.

import platform
import os

# Check the OS and clear the screen as per the OS.

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

# Display string at left hand side.

print(f"\n{user_input_string.ljust(50)}")
print(f"{user_input_string.center(50)}")
print(f"{user_input_string.rjust(50)}\n")

# Display final statement to show the end of the script.

print(f"The string is displayed at center, left & right hand side of the screen as above. That's it for now.\n")
