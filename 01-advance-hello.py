# Python script to detect the OS and then clear screen and then print messages at short time intervals.

# Import modules.

import platform     # To check the OS type.
import os           # To execute the OS command to clear screen.
import time         # To introduce small time interval by sleep function.

# Check which OS.

os_name = platform.system()

# Clear screen as per the OS type.

if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Print message at short time intervals.

print("Hi there!")  # Print message.
time.sleep(2)       # Sleep for 1 second.
print("I am the Python interpreter.")
time.sleep(2)
print("Welcome to the world of python! It'll be fun!")
time.sleep(2)