#arranging a list so that the adjacent contents of the list are not repetitive

arr = [1, 1, 1, 2, 2, 2,4,3,4]
unique_arr = {}
lra = []

length = len(arr)
print(length)

for i in arr:
    if i not in unique_arr:
        unique_arr[i] = arr.count(i)

print("Dict", unique_arr)

while len(lra) < length:
    for i in unique_arr:
        if unique_arr[i] > 0:
            lra.append(i)
            #print("lra ", len(lra))
            unique_arr[i] = unique_arr[i] - 1

print(lra)
