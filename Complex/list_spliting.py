#python program that splits a list in two halfs

def split_list(input_list):
    length = len(input_list)
    half = length // 2
    
    # Split the list into two halves
    first_half = input_list[:half]
    second_half = input_list[half:]
    
    return first_half, second_half


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Splitting the list
first, second = split_list(list)
print("First half:", first)
print("Second half:", second)
