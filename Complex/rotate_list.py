def rotate_left(lst, positions):
    # Calculate the effective number of positions to rotate
    effective_rotation = positions % len(lst)
    
    # Perform the rotation using list slicing
    rotated_list = lst[effective_rotation:] + lst[:effective_rotation]
    
    return rotated_list

# Example list
my_list = [1, 2, 3, 4, 5]

# Number of positions to rotate left
positions_to_rotate = 2

result = rotate_left(my_list, positions_to_rotate)
print(result)
