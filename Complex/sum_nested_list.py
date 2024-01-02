#a python file that sums all the integers in a or a nested list

def sum_nested_list(nested_list):
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):
            total_sum += sum_nested_list(element)  # Recursively call the function for nested lists
        else:
            total_sum += element 
    return total_sum


my_list = [1, 2, [3, 4, [5, 6]], 7, [8, 9, 10]]

result = sum_nested_list(my_list)
print("Sum of all numbers in the nested list:", result)
