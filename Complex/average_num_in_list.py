def calculate_average(num_list):
    total = sum(num_list)
    count = len(num_list)
    
    if count == 0:
        return 0  # To handle an empty list
    
    average = total / count
    return average

# Example list of numbers
my_numbers = [10, 20, 30, 40, 50]

# Calculating the average
result = calculate_average(my_numbers)
print("The average is:", result)
