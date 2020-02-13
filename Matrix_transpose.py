from functools import reduce

a = [[40, 62, 76, 36],
     [74, 14, 36, 16],
     [23, 57, 15, 54],
     [89, 19, 67, 48]]

b = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
k = 0

print(len(a))
for i in a:
    print(i, i[2])
    for j in range(len(i)):
        b[j][k] = i[j]
    k = k + 1


'''for row in b:
    print(row)'''
print("transposed matrix: ",b)

sort_matrix, diag = [], []
for i in range(len(a)):
    for j in range(len(a[i])):
        sort_matrix.append(a[i][j])

sort_matrix.sort()
print('sort_matrix', sort_matrix)

#g = sort_matrix.pop()
#print(g)
for i in range((len(a)-1),-1,-1):
    for j in range((len(a[i])-1),-1,-1):
        a[i][j] = sort_matrix.pop()
        #print(a[i][j])
print("sorted matrix:",a)


if len(a) == len(a[0]):
    print("equal matrix")
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j:
                diag.append(a[i][j])
#    print(diag)

    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j:
                a[i][j] = diag.pop()

    for i in range((len(a) - 1), -1, -1):
        for j in range((len(a[i]) - 1), -1, -1):
            if i + j == 3:
                diag.append(a[i][j])

    for i in range((len(a) - 1), -1, -1):
        for j in range((len(a[i]) - 1), -1, -1):
            if i + j == 3:
                a[i][j] = diag.pop()

    print(a)