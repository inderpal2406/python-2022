# This script will accept two numbers from user, then add them and give the result.

# Import modules.

import platform
import os

# Clear the screen as per the OS type.

os_name=platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")
else:
    print(f"The OS is not Windows/Linux. This script is designed only for Windows/Linux. Hence exiting.")
    exit()

# Display purpose of the script.

print(f"This script will accept 2 numbers and display their sum.\n")

# Accept user input.

num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))

# Calculate sum.

sum=num1+num2

# Display the sum.

print(f"\nThe sum of {num1} and {num2} is {sum}.\n")