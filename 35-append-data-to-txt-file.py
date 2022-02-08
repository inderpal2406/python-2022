# This script will apppend data to an already existing txt file txt-files\file5.txt.

content_list = ["This is fourth line.","This is fifth line."]

fo = open("txt-files\\file5.txt","a")

for each_line in content_list:
    fo.write(each_line+"\n")

fo.close()

print(f"The content from the list is appended to the txt-files\\file5.txt file.")

# If the file didn't exist, then append mode would have created the file and written data to it (just like write mode).
# If the file already exists, then append mode will append data to it.
# If the file didn't exist, then write mode would create the file and write data to it.
# If the file already exists, then write mode would delete it, then write data to it (overwrite).
