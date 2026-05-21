'''
Remove all vowels from a string.
'''
n = input("Enter a string: ")
vowel = "aeiou"
s = [x for x in n if x not in vowel]
print(f"string without vowels is: {"".join(s)}")