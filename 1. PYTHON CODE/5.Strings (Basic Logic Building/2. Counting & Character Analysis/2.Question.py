'''
Count the number of digits, letters, and special characters in a string.
'''
str1 = input("Enter a string: ")
digits = letters = special_characters = 0
for char in str1:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
    elif not char.isspace():
        special_characters += 1
print(f"Digits: {digits}")
print(f"Letters: {letters}")
print(f"Special Characters: {special_characters}")
