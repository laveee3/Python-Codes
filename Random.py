import random
import time
num1 = [1,2,3,4]
num2 = [1,2,3,4,5,6]
dice1 = random.randrange(1,5)
dice2 = random.shuffle(num1)
print(dice2)

random.seed(10)
print(random.random())

print(random.randrange(3, 9))
#returns a number between 3 (included) and 9 (not included)

print(random.randint(3, 9))
#returns a number between 3 and 9 (both included)

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))

print(random.random())
#The random() method returns a random floating number between 0 and 1.

print(random.uniform(20, 60))
#uniform()	Returns a random float number between two given parameters


time.sleep(2)
print("-----")
for i in range(4):
    print(random.random())