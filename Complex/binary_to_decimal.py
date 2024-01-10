#python program to turn binary numbers to decimal 


def binary_to_decimal(binary):
    decimal = 0
    power = 0

    # Iterating through the binary digits in reverse order
    for digit in reversed(binary):
        if digit == '1':
            decimal += 2 ** power  # Adding the contribution of each digit to the decimal value
        power += 1

    return decimal

binary_number = "10101"
decimal_number = binary_to_decimal(binary_number)
print(f"The decimal equivalent of {binary_number} is: {decimal_number}")
