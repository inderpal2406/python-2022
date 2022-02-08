# This script will create a txt file as txt-files\file2.txt and add content to it.

fo = open("txt-files\\file2.txt","w")
fo.write("This is the first line.")
fo.close()

print(f"The file txt-files\\file2.txt is created and content is added to it.")
