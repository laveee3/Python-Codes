

\
\
# write a python program to find unique numbers and group same number together in a list
array = [0,1,2,1,2,0,2,3]
unique_array = []
dutch_flag = []
count = []
for i in array:
    if i not in unique_array:
        unique_array.append(i)
        count.append(array.count(i))
print(unique_array, count)


for i in unique_array:
    a = count[i]
    while a > 0:
        dutch_flag.append(i)
        a = a - 1

print(dutch_flag)

