# Script to practise text file operations.

# Initialize variables.

file = ".\\txt-files\\file2.txt"

# Write one single line to the file using write() function.

fileobj = open(file,"w")
fileobj.write("This is first line.")
fileobj.close()

# Write three lines using write() function.

fileobj = open(file,"w")
fileobj.write("This is first line.")
fileobj.write("This is second line.")
fileobj.write("This is third line.")
fileobj.close()

# write() when invoked, will see where is the cursor in the file,
# and then start writing from there. Multiple invocations won't 
# automatically print to next line.

# Write three lines using write() function on separate lines.

fileobj = open(file,"w")
fileobj.write("This is first line.\nThis is second line.\nThis is third line.\n")
fileobj.write("This is fourth line.\n")
fileobj.close()

# Write multiple lines to a file from a list.

data_list = ["This is first line.","This is second line.","This is third line."]
fileobj = open(file,"w")
fileobj.writelines(data_list)
fileobj.close()

# writelines() function will take data from list and write it to the file.
# It will simply write all the list items to the file.
# If a newline character is there in any of the list items, then cursor 
# is transferred to next line, and then writelines() would continue to 
# write the remaining list items on the new line.

# Write multiple lines on separate lines to a file from a list.

data_list = ["This is first line.\n","This is second line.\n","This is third line.\n"]
fileobj = open(file,"w")
fileobj.writelines(data_list)
fileobj.close()

# Write multiple lines on separate lines to a file from a list,
# but each list item won't have new line character.

data_list = ["This is first line.","This is second line.","This is third line.","Fourth line."]
fileobj = open(file,"w")
for each_item in data_list:
    fileobj.write(each_item+"\n")
fileobj.close()
