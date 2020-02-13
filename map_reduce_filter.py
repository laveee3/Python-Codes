# -*- coding: utf-8 -*-
""" Created on Mon Nov 25 21:23:49 2019
@author: lavan """

#filter(func, iterable): Return an iterator yielding those items of iterable for which func(item) is True. For example,
lst = [11, 22, 33, 44, 55]
filter(lambda x: x % 2 == 0, lst)  # even number
list(filter(lambda x: x % 2 == 0, lst))  # Convert filter object to list [22, 44]
for item in filter(lambda x: x % 2 == 0, lst): print(item, end=' ') #22 44
print(filter(lambda x: x % 2 == 0, lst))  # Cannot print() directly <filter object at 0x6ffffe797b8>


#map(func, iterable): Apply (or Map or Transform) the function func on each item of the iterable. For example,
lst = [11, 22, 33, 44, 55]
map(lambda x: x*x, lst)   # square  <map object at 0x7fc46f72b908>
list(map(lambda x: x*x, lst))  # Convert map object to list  [121, 484, 1089, 1936, 3025]
for item in map(lambda x: x*x, lst): print(item, end=' ')  #121 484 1089 1936 3025
print(map(lambda x: x*x, lst))  # Cannot print() directly? <map object at 0x6ffffe79a90>

#reduce(func, iterable) (in module functools): Apply the function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value, also known as aggregation. For example, lst = [11, 22, 33, 44, 55] 
from functools import reduce
p = reduce(lambda x,y: x+y, lst)  # aggregate into sum  165    # (((11 + 22) + 33) + 44) + 55
print("reduce ", p)

#filter-map-reduce: used frequently in big data analysis to obtain an aggregate value.
# Combining filter-map to produce a new sub-list
new_lst = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, lst)))
print(new_lst)  #[484, 1936]

# Combining filter-map-reduce to obtain an aggregate value
from functools import reduce
q = reduce(lambda x, y: x+y, map(lambda x: x*x, filter(lambda x: x % 2 == 0, lst)))
#q = reduce(lambda x, y: x*y, map(lambda x: x*x, filter(lambda x: x % 2 == 0, lst)))
print ("nested lambda- reduce,filter:", q)
#List comprehension: a one-liner to generate a list as discussed in the earlier section. e.g.,


lst = [3, 2, 6, 5]
new_lst = [x*x for x in lst if x % 2 == 0]
print(new_lst) #[4, 36]

# Using Lambda function
f = lambda x: x*x    # define a lambda function and assign to a variable
new_lst = [f(x) for x in lst if x % 2 == 0]  # Invoke on each element
print(new_lst) #[4, 36]

new_lst = [(lambda x: x*x)(x) for x in lst if x % 2 == 0]  # inline lambda function
print(new_lst) #[4, 36]


'''Enumerate() in Python
A lot of times when dealing with iterators, we also get a need to keep a count of iterations. 
Python eases the programmers’ task by providing a built-in function enumerate() for this task. 
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
This enumerate object can then be used directly in for loops or be converted into a list of tuples 
using list() method.'''

l1 = ["eat","sleep","repeat"] 
s1 = "geek"
print (list(enumerate(l1)) )
print (list(enumerate(s1,2)))

