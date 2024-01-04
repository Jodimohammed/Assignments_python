#python file that sums every third number in a list 

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

third_num_total = 0

for num in list:
    
    if num % 3  == 0:
        third_num_total += num
    
print(third_num_total)

