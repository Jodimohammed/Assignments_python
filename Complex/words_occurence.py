string = "jodi is a jodi by a jodi"
words = string.split()
word_count = 0 
print(string)
word_find = input("Please enter the word to cont in the string above:")

for word in words :
    if word == word_find:
        word_count += 1
        
print(f'the number of times  "{word_find}" appears in the string is: {word_count}')

