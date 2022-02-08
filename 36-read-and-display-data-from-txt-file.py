# This script will read and display data from txt-files\file5.txt.

fo = open("txt-files\\file5.txt","r")
print(fo.read())
fo.close()

'''
# Or data can be stored in a variable when read and then displayed.

fo = open("txt-files\\file5.txt","r")
data = fo.read()
fo.close()
print(f"{data}")

'''
