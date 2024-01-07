#A python program to flaten a nested list. 

def flaten_nested_list(nested_list):
    flatened_list = []
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                    flatened_list.append(item)

        else:
            flatened_list.append(element)
    return flatened_list


my_list = [1, 2, [3, 4],[5,6], 7, [8, 9, 10]]

result = flaten_nested_list(my_list)
print( result)
