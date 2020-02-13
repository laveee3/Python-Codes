"""Spyder Editor
#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print (s)

print ("The dimensions of the object:")
print (s.ndim)"""

#import pandas as pd
import numpy as np

a = np.array([1,2,3]) 
print (a)


# more than one dimensions 
b = np.array([[1, 2], [3, 4]]) 
print (b)


# minimum dimensions 
c = np.array([1, 2, 3,4,5], ndmin = 1) 
print(c)

d = np.array([1, 2, 3,4,5], ndmin = 3) 
print(d)

# dtype parameter 
e = np.array([1, 2, 3], dtype = complex)
print(e)

#ndarray.shape - This array attribute returns a tuple consisting of array dimensions. 
f = np.array([[1,2,3],[4,5,6]]) 
print(f.shape)

#It can also be used to resize the array.
g = np.array([[1,2,3],[4,5,6]]) 
g.resize(3,2)
print(g)

#ndarray.ndim - This array attribute returns the number of array dimensions.
h = np.arange(24) 
print(h)

i = h.reshape(2,4,3) 
print(i)

# array of five zeros. Default dtype is float 
j = np.zeros(5) 
print (j)

k = np.ones((5,), dtype = np.int) 
print (k)
# there is no twos like np.twos(5) 

'''numpy.asarray
This function is similar to numpy.array except for the fact that it has fewer parameters. 
This routine is useful for converting Python sequence into ndarray.'''

x = [1,2,3] 
l = np.asarray(x) 
print(l)

#x = np.arange(10,20,2)  output = [10 12 14 16 18]
#numpy.arange(start, stop, step, dtype)
#numpy.linspace(start, stop, num, endpoint, retstep, dtype)
#numpy.logspace(start, stop, num, endpoint, base, dtype)

m = np.arange(10) 
n = slice(2,7,2) 
print(m[n])
#[2  4  6]
# same answer when n = m[2:7:2] 

