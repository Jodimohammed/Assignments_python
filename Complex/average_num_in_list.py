#python program to calculate the average num in a list 

def calculate_average(num_list):
    total = sum(num_list)
    count = len(num_list)
    
    if count == 0:
        return 0  
    else:
        average = total / count
    return average


my_numbers = [10, 20, 30, 40, 50]

result = calculate_average(my_numbers)
print("The average is:", result)
