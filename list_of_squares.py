#python file to print out squared numbers in a list and put it in another list
list = [1,2,3,4,5,6,7,8,9,10]
list_2 = []

for num in list:
    list_2.append(num**2)
    #print(num**2)
    
print(list_2)
