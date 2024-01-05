my_list = [1, 2, 2, 3, 4, 4, 5]
my_list_without_duplicates = []
for item in my_list:
    if item not in my_list_without_duplicates:
        my_list_without_duplicates.append(item)
print(my_list_without_duplicates)







my_list = [1, 2, 2, 3, 4, 4, 5]
my_list_without_duplicates = list(set(my_list))
print(my_list_without_duplicates)
