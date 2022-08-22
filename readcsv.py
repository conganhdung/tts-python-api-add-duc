import csv
from collections import defaultdict
columns = defaultdict(list)
with open("Contact.csv") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

print(type(list(columns["name"][1].split())))
print(columns['phone'])
print(columns['street'])
