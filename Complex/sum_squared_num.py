#python file to add up all  squared numbers in a list 
list = [1,2,3,4,5,6,7,8,9,10]

list_squared = []


square_total = 0
for num in list:
    
    list_squared.append(num**2)
    square_total += num**2
 
print("The squared list: " , list_squared)   
print("------------------")
print("Total sum of the list: " , square_total)
    