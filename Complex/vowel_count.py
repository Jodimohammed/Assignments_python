#python program that count the amount of vowels in a string

def count_vowels(input_string):
    vowels = "aeiouAEIOU" 
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_str = "Hello, how are you?"
result = count_vowels(input_str)
print(f"The number of vowels in '{input_str}' is: {result}")
