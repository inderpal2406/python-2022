# This script will display current date and time.

# Import modules.

import time

# Display date.

todays_date=time.strftime("%d-%m-%Y")
print(f"Today's date: {todays_date}")

# Display time.

current_time=time.strftime("%H:%M:%S")
print(f"Current time: {current_time}")
