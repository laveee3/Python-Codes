#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

#Series
data = np.array(['a','b','c','d','e'])
s = pd.Series(data)
print (s)
#retrieve the first element:       print s[0]
#retrieve the first three element: print s[:3]
#retrieve the last three element:  print s[-3:]

s = pd.Series(data,index=[100,101,102,103])
print (s)

#A dict can be passed as input and if no index is specified, then the dictionary keys are taken in a sorted order to construct index.
data1 = {'a' : 0., 'b' : 1., 'c' : 2.}
r = pd.Series(data1)
print (r)

q = pd.Series(data1,index=['b','c','d','a'])
print (q)

'''
Create DataFrame
A pandas DataFrame can be created using various inputs like −
Lists, dict, Series, Numpy ndarrays, Another DataFrame'''

data2 = [1,2,3,4,5]
df = pd.DataFrame(data2)
print (df)

data3 = [['Alex',10],['Bob',12],['Clarke',13]]
df1 = pd.DataFrame(data3,columns=['Name','Age'])
print (df1)

data4 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df2 = pd.DataFrame(data4)
print (df2)