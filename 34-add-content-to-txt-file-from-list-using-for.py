# In this script we'll add content to a txt file from a list using a for loop.

# Define list having the content. Here we didn't add \n in each list member.

content_list = ["This is first line.","This is second line.","This is third line."]

# Write content to the txt file.

fo = open("txt-files\\file5.txt","w")

for each_line in content_list:
    fo.write(each_line+"\n")

fo.close()

print(f"The content from the list is added to the txt-files\\file5.txt using a for loop.")

# In this way we added \n automatically.
