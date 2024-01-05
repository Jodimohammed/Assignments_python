#rotating a list to left with a number of giving positions


def rotate_left(list, positions):
    # Calculate the effective number of positions to rotate
    effective_rotation = positions % len(list)
    
    # Perform the rotation using list slicing
    rotated_list = list[effective_rotation:] + list[:effective_rotation]
    
    return rotated_list


my_list = [1, 2, 3, 4, 5]

# Number of positions to rotate left
positions_to_rotate = 4

result = rotate_left(my_list, positions_to_rotate)
print(result)
