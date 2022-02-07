# This script will read a string form the user and print its characters one by one with index values.

# Import modules.

import clear_screen_module

# Clear the screen.

clear_screen_module.clear_screen()

# Print the purpose of the script.

print(f"This script will accept a string and display its characters one by one along with index values.\n")

# Accept the string from the user.

user_str = input("Enter the string: ")

# Display the characters of the string one by one along with index values.

for i in user_str:
    print(f"{i} --> at index {user_str.index(i)}")
