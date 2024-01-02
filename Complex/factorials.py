#python file that prints out the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("please enter a number to find the factorial: "))
print()
result = factorial(number)
print(f"The factorial of {number} is: {result}")
