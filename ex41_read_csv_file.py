# Script to read data from a CSV file.

import csv

# Read CSV file with default limiter comma.

file = "csv-files\\file1.csv"
fileobj = open(file,"r")
content = csv.reader(fileobj,delimiter=",")
#print(f"{type(content)}")
print("\nContent of file1.csv with delimiter as , is:")
for each in content:
    print(f"{each}")
fileobj.close()

# Read CSV file with | as delimiter.

file = "csv-files\\file2.csv"
fileobj = open(file,"r")
content = csv.reader(fileobj,delimiter="|")
print("\nContent of file2.csv with delimiter as | is:")
for each in content:
    print(f"{each}")
fileobj.close()
