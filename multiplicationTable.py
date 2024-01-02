# python file for multiplication table 
num = int(input("please enter a number: "))


for i in range(1,11):
    product = i * num
    print("{} * {} = {}".format(num,i,product))