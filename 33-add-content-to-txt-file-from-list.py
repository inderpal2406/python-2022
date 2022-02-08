# In this script, instead of writing each line to the txt file,
# we'll add the lines to the txt file from a list.

# Define list of our content/lines.

content_list = ["This is first line.\n","This is second line.\n","This is third line.\n"]

# Create and write to the txt file.

fo = open("txt-files\\file4.txt","w")
fo.writelines(content_list)
fo.close()

print(f"The lines from the list are added to the file txt-files\\file4.txt.")

# It is not a good practice to mention \n in each of the list members. 
# We'll see to enhance this in next script by adding \n automatically.
