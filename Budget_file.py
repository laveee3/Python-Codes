
#import pandas as pd
import csv

LocationR = r"C:\Users\lavan\Desktop\budget\readf.csv"
LocationA= r"C:\Users\lavan\Desktop\budget\addf.csv"
LocationW= r"C:\Users\lavan\Desktop\budget\writef.csv"
#df = read_csv(Location)


#if we want to open a file and read line by line

f1 = open(LocationR, "r")
f2 = open(LocationA, "a+")
f3 = open(LocationW, "w")

for line in f1:
   line = line.rstrip() # to remove \n that exists at the end of the line in all text n csv files
   splitText = line.split(",") #now splitText[i] has column[i] info
   print(splitText[0],splitText[1])
   f3.write(line+"\n")
   f2.write(line + "\n")

   """for line2 in f2:
      if (splitText[0] == line2):
         print("hi")
         f2.write(line + "\n")"""

  # f3.write("\n")

fclose(f1)
fclose(f2)
fclose(f3)

#end