'''
Print the sentence in title case (first letter capital, rest lowercase).
'''
n = input("Enter a sentence: ")
s = n.split()
for i in range(len(s)):
    s[i] = s[i].capitalize()
print(" ".join(s))