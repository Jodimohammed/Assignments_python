#python program to find the longest word in  a STRING 

def longest_word(string):
    words = string.split()  # Split the string into words
    longest = max(words, key=len)  # Find the longest word using the max function and len as the key
    return longest

input_string = "This is a string with some long and shorter words"
longest = longest_word(input_string)
print(f"The longest word is: {longest}")
