import csv
import pandas as pd
'''
# this code works but only reason it is not used in visio lending is baecause it cannot be passed as an argument of a class
csv_reader = []
with open('rules.csv', 'rt') as f:
    csv_reader = csv.DictReader(f, escapechar='\\')

    for row in csv_reader:
        #print(dict(row.name))
        print(row["Rate "])
        print(dict(row))
        print(row[Rate])

        if row["State"] is not null:
           if row["Disqualified"] is not null:
               self.state == row["State"]
               self.disqualified = row["Disqualified"]
           else:
               self.state == "Florida"
               self.Rate = row["Rate"]
#--------------------

# cannot read the column name by below code
LocationR = r"C:\Data\InterviewPrep\Python_Practice\rules.csv"
csv_reader = open(LocationR, "r")

'''
article_read = pd.read_csv('Large_Sales_Original.csv')

print (article_read.head())
#print (article_read[['Title','Author']])
print (article_read.count())

str1 = ">720"
str2 = 710



