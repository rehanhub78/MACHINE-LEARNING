'''
Count how many uppercase and lowercase letters a string has.
'''
str1 = input("Enter a string: ")
uppercase = 0
lowercase = 0
for char in str1:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
print(f"Uppercase Letters: {uppercase}")
print(f"Lowercase Letters: {lowercase}")