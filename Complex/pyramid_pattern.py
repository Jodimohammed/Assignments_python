#python program that prints a pyramid pattern with a given height

def print_pyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2* i - 1))

pyramid_height = int(input("Enter the height of the pyramid: "))

print_pyramid(pyramid_height)
