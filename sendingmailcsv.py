import csv, smtplib, ssl
from collections import defaultdict
from unicodedata import name
message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
from_address = "nguyenminhduc.jvb@gmail.com"
password = "wiuurcuovguhawgt"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    # file = '/home/majinbuu/Python Test/python-api-test2/data_contact.csv'
    columns = defaultdict(list)
    with open("Contact.csv") as file:
        # reader = csv.reader(file)
        reader = csv.DictReader(file) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v) # append the value into the appropriate list
                                    # based on column name k
        # print((columns["email"]))
        for i in range(len(columns["email"])):
            # print (columns["name"][i])
            # print((columns["email"]))
        
            server.sendmail(
                from_address,
                columns["email"][i],
                message.format(name=(columns["name"][i]),grade= (columns["grade"][i])),
    )