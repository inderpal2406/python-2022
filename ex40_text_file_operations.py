# Script to perform operations on a text file

# Create an empty file.

fileobj = open("txt-files\\file1.txt","w")
#fileobj.close()  # It gives an error if file is closed before below operations. 
print(f"File name is: {fileobj.name}")
print(f"File is opened in {fileobj.mode} mode.")
print(f"Is file opened in readable mode: {fileobj.readable()}")
print(f"Is file opened in writable mode: {fileobj.writable()}")
fileobj.close()

# Write a single line to the file.

fileobj = open("txt-files\\file1.txt","w")
fileobj.write("This is first line.")
fileobj.close()

# Write multiple lines to the file.

fileobj = open("txt-files\\file1.txt","w")
fileobj.write("This is first line.\nThis is second line.\n")
fileobj.close()

# Write multiple lines to the file from a list.

data = ["First line from list.\n","Second line from list.\n"]
fileobj = open("txt-files\\file1.txt","w")
fileobj.writelines(data)
fileobj.close()

# Write multiple lines from list without having \n in list items.

data = ["First line from list without \\n.","Second line from list without \\n."]
fileobj = open("txt-files\\file1.txt","w")
for each_item in data:
    fileobj.write(each_item+"\n")
fileobj.close()

# Read and display all content of the file.

fileobj = open("txt-files\\file1.txt","r")
print("\nThe file data is:")
print(f"{fileobj.read()}")
fileobj.close()

# Read and display all content of the file with a variable.

fileobj = open("txt-files\\file1.txt","r")
data = fileobj.read()
fileobj.close()
print(f"\nThe file data is:\n{data}")

# Read one line at a time and display.

fileobj = open("txt-files\\file1.txt","r")
print("\nThe file data read one line at a time is:")
print(f"{fileobj.readline()}")
print(f"{fileobj.readline()}")  # how does the second call of readline() reads second line automatically?
fileobj.close()

# Read entire file data into a list and display all lines with one line at a time.

fileobj = open("txt-files\\file1.txt","r")
content_list = fileobj.readlines()
fileobj.close()
print("\nThe file data is:")
for each_item in content_list:
    print(each_item)
# Print the first line only.
print(f"\nThe first line is: {content_list[0]}")
# Print the last line only.
print(f"\nThe last line is: {content_list[-1]}")
# Print the second line only.
print(f"The second line is: {content_list[1]}")

# Append line to existing file.

fileobj = open("txt-files\\file1.txt","a")
fileobj.write("This line is appended.\n")
fileobj.write("One more line is appended.\n")
fileobj.close()
# If I run above code multiple times, then the lines won't get appended.
# Perhaps it sees that if we are appending the same line again and doesn't do it then.
# Similarly, we can append lines with fileobj.writelines() function as well using a list.
