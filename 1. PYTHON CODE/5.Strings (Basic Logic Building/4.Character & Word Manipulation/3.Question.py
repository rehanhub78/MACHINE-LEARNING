'''
Replace all vowels with '*'.
'''
n = input("Enter a string: ")
vowels = "aeiou"
s = list(n)
for i in range(len(s)):
    if s[i] in vowels:
        s[i] = "*"
print(f"New string is: {"".join(s)}") 