#python file that checks if a number is prime

def is_prime(num):
    if num <= 1:
        return False
    num_pwr =int(num ** 0.5) + 1
    for i in range(2, num_pwr):
        if num % i == 0:
            return False
    return True


number = int(input("please enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")