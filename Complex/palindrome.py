#python file to check if a string is palindrome

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase 
    s = ''.join(e.lower() for e in s if e.isalnum())
    return s == s[::-1]

string = "Apapa!"
result = is_palindrome(string)

if result:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")
