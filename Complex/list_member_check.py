fir_list = [1,2,3,4,5]
sec_list = [1,2,9,5,0]

common_mem = []

print(fir_list)
print(sec_list)

for item in fir_list:
    if item in sec_list:
        common_mem.append(item)
        
print("the common members between both list is/are: ",common_mem)



