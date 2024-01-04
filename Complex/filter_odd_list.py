#python file that removes odd number from a list

list = [1,2,3,4,5,6,7,8,9,10]

print(list)


for index , num in enumerate(list):
    if num % 2  != 0:
        list.pop(index)
        
print(list)
        
    

