#A python program to flaten a nested list. 

def flatten_nested_list(nested_list):
    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                    flattened_list.append(item)

        else:
            flattened_list.append(element)
    return flattened_list


my_list = [1, 2, [3, 4],[5,6], 7, [8, 9, 10]]

result = flatten_nested_list(my_list)
print( result)
