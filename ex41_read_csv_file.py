# Script to read data from a CSV file.

import csv

file = "csv-files\\file1.csv"
fileobj = open(file,"r")
content = csv.reader(fileobj,delimiter=",")
#print(f"{type(content)}")
for each in content:
    print(f"{each}")
fileobj.close()
