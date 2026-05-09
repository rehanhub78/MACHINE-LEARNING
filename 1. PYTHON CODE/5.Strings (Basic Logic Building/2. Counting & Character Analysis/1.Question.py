'''
Count how many vowels and consonants are in a string.
'''
str1 = input("Enter a string: ")
vowels = 0
consonants = 0
for char in str1:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")