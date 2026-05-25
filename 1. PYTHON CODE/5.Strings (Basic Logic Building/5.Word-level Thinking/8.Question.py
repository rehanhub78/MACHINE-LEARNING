'''
Capitalize the first letter of each word.
'''
n = input("Enter a sentence: ")
s = n.split()
for i in range(len(s)):
    s[i] = s[i][0].upper() + s[i][1:]

print(" ".join(s))
