# Program tht takes array for daily stock price and returns max profit that could be made by buying and selling
stk_price = []
num = input("Enter how many stock elements you want:")
d = int(num)
print('Enter numbers in array: ')
for i in range(d):
    n = int(input("num :"))
    stk_price.append(int(n))
print(stk_price)
'''
stk_price = [310,315,275,290,270,230,255,250]
num = len(stk_price)'''

low_index, high_index, max_profit = 0,0,0

def find_max(stk_price):
    size = len(stk_price)
#    print ("size of array is:",size)
    index, profit = 0, 0

    for i in range(1,size-1):
        if (stk_price[0] < stk_price[i]):
            diff = stk_price[i] - stk_price[0]
            if diff > profit:
                index = i
                profit = diff
    #print(index, profit)
    return (index, profit)

#print("index, profit:")
#find_max(stk_price)

for p in range(d):
    #print("index, profit:")
    #print(stk_price[i:])
    j, d = find_max(stk_price[p:])
    #print(j,d)
    if (d > max_profit):
        low_index = p
        high_index = j + p
        max_profit = d

print("low_index, high_index, max_profit", stk_price[low_index], stk_price[high_index], max_profit)