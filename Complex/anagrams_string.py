#python program to check for anagrams in a list

def anagrams(str1, str2):
    # Remove spaces and punctuation, convert to lowercase
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()

    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)


    return sorted_str1 == sorted_str2


string1 = "listen"
string2 = "silent"
print(anagrams(string1, string2))  

string3 = "hello"
string4 = "world"
print(anagrams(string3, string4))  
