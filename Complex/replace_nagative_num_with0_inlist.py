#python program that replace the negative numbers in a list to 0

def replace_negative_with_zero(lst):
    return [max(0, num) for num in lst]



numbers = [5, -3, 10, -8, 0, -2]
result = replace_negative_with_zero(numbers)
print(f"List with negative numbers replaced by zero: {result}")

