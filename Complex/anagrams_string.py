def are_anagrams(str1, str2):
    # Remove spaces and punctuation, convert to lowercase
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()

    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2

# Test cases
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True

string3 = "hello"
string4 = "world"
print(are_anagrams(string3, string4))  # Output: False
