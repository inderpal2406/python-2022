"""Module to remove spaces from the thumbprint string of an SSL certificate"""

# This script will remove spaces from the thumbprint string of an SSL certificate.

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script will remove spaces from thumbprint string of SSL certificate.\n")
    thumbprint = "ba 0e 74 9e 28 98 c0 10 b8 80 25 bd 85 10 03 44 25 00 d1 5e"
    our_list = thumbprint.split(" ")
    #print(f"{len(our_list)}")
    print(f"Old thumbprint = {thumbprint}")
    print(f"No. of chars in old thumbprint: {len(our_list)*2}\n")
    new_thumbprint = ''.join(our_list)
    print(f"New thumbprint = {new_thumbprint}")
    print(f"No. of chars in new thumbprint: {len(new_thumbprint)}\n")
    #for each_item in our_list:
    #    print(f"{each_item}")
    return None

# Call main function if the script is executed.

if __name__ == "__main__":
    main()
