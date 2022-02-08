# This script would create an empty text file txt-files\file1.txt, provided txt-files directory pre-exists.
# This script is designed only for windows system for now.

# Create the empty text file.

fo = open("txt-files\\file1.txt","w")
fo.close()
print(f"New txt file created as txt-files\\file1.txt.")
