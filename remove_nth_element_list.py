#remove the last value in a list 

import random

list = []
for i in range(1,11):
    list.append(random.randint(1,10))




print(list)
list.pop(-1)
print(list)
