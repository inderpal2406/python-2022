# This script will print the machine info on which this script is executed.

# Import modules.

import clear_screen_module
import platform
import getpass

# Clear the screen.

clear_screen_module.clear_screen()

# Print purpose of the script.

print(f"This script will display the machine information.\n")

# Print the machine information.

print(f"Machine hostname: {platform.node()}")
print(f"Operating system: {platform.system()}")
print(f"Operating system version: {platform.platform()}")
print(f"Processor information: {platform.processor()}")
print(f"Processor architecture: {platform.architecture()[0]}")
print(f"Current user: {getpass.getuser()}\n")
