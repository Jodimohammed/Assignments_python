#python file to find all prime numbers less than 100

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find all prime numbers less than 100 and put them in a list 
prime_numbers = [num for num in range(2, 100) if is_prime(num)]

print("Prime numbers less than 100:")
print(prime_numbers)
