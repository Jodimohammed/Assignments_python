def contains_only_digits(s):
    return s.isdigit()

string1 = "12345"
string2 = "12A34"

print(f"Does string1 contain only digits? {contains_only_digits(string1)}")
print(f"Does string2 contain only digits? {contains_only_digits(string2)}")