#python program to capitalize first letter of a word in a string 

def capitalize_first_letter(string):
    return string.title()




input_sentence = "this is a sample sentence"
capitalized = capitalize_first_letter(input_sentence)
print(f"Capitalized sentence: {capitalized}")
