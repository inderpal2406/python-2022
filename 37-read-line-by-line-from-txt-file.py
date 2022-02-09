# This script will read line by line from the txt-files\file5.txt file and display it.

fo = open("txt-files\\file5.txt","r")
print(f"{fo.readline()}")   # Read first line and print it.
print(f"{fo.readline()}")   # Read second line and print it.
fo.close()

'''
OR, below code can also be used to read the line, then store it in a variale and then display it.
fo = open("txt-files\\file5.txt","r")
first_line = fo.readline()
second_line = fo.readline()
print(f"{first_line}{second_line}")
'''

# It seems, the read function reads the line with the special character at the end (\n).
# That is why it is displayed automatically in the output of second alternative code block.
# This is seen in double spacing between the lines in output of first code block.
