#python list that filters all number greater than 10 in a list and puts it in another list 

import random

random_list = [random.randint(1,50) for _ in range(10)]  

print("Random List:", random_list)

print()

greater_than10 = []

for num in random_list :
    if num > 10:
       greater_than10.append(num) 
       

print("Numbers greater than 10 in the list: " ,greater_than10)