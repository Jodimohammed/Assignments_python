#python list that counts all even numbers in a list

import random

# Generating a random list of numbers  and then  putting them in a list
random_list = [random.randint(1,50) for _ in range(10)]  

# Counting the number of even numbers in the list
even_num_count = sum(1 for num in random_list if num % 2 == 0)

print("Random List:", random_list)
print("Number of even numbers in the list:", even_num_count)