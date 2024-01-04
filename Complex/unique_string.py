#python program that prints out the unique letters in a string

def unique_letters(input_string):
    unique = []
    for char in input_string:
        if char.isalpha() and char.lower() not in unique:
            unique.append(char.lower())

    print("Unique letters in the string:", *unique)



input_str = "Hello, how are you"
unique_letters(input_str)
