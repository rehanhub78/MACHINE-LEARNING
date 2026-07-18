'''
Print characters that are common in two strings.
'''
str1 = "Hello World"
str2 = "World Hello"
common = []
for char in str1:
    if char in str2 and char not in common:
        common.append(char)
print(f"Common characters: {', '.join(common)}")