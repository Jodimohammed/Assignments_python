#python file print out the amount of even numbers in a list
#uncomment the print statement on line 9 to print out the items in the list. 
import random

list = []
for i in range(1,11):
    list.append(random.randint(1,10))

print(list)
for num in list:
    if num%2==0:
        print(num)
