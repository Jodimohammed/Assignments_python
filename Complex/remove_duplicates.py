#python program to remove duplicates in a list 

#using for loop 
list_duplicates = [1, 2, 2, 3, 4, 4, 5]

list_without_duplicates = []
for item in list_duplicates:
    if item not in list_without_duplicates:
        list_without_duplicates.append(item)
        
print(list_without_duplicates)

#using set method in python
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list_without_duplicates = list(set(my_list))
print(my_list_without_duplicates)
