# This is a custom module (python script) to clear the terminal as per the OS type.
# This module can be imported into other scripts, where there is a need to clear the screen.

# Import modules.

import platform
import os

# Define fucntion to detect the OS type and clear the screen.

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
