#python program to check if number is even without using the % operator

def is_even(num):
    return (num & 1) == 0

num = 10  

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
