# This script will add content to the empty file txt-files\file1.txt which was created in previous script 29-txt-file-creation.py.

fo = open("txt-files\\file1.txt","w")
fo.write("This is the first line.")
fo.close()
print(f"First line is added to the file txt-files\\file1.txt.")
