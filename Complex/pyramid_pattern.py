def print_pyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

# Example height of the pyramid
pyramid_height = 5

# Printing the pyramid
print_pyramid(pyramid_height)
