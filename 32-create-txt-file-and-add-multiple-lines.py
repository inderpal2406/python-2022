# This script will create a txt file txt-files\file3.txt and add multiple lines to it.

fo = open("txt-files\\file3.txt","w")
fo.write("This is the first line.\nThis is the second line.\n")
fo.close()

print(f"The file txt-files\\file3.txt is created and multiple lines are added to it.")

# Important Note: If we run this script again and again, then same file will be created again and same content would be added to it.
# Whenever, python opens a file in write mode, it'll check if the file pre-exists.
# If the file pre-exists, then it'll delete it first and then create a new file (As per the Udemy instructor).

