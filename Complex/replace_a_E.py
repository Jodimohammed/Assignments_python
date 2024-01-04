#python program that replaces a with e in a string

def replace_a_with_e(string):
    replaced_string = string.replace('a', 'e')
    return replaced_string


original_str = "I have a nice bag ."


replaced_str = replace_a_with_e(original_str)
print("Original String:", original_str)
print('------------------------------')
print("String with 'a' replaced by 'e':", replaced_str)
