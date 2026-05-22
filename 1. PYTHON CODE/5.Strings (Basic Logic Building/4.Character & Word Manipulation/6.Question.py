'''
Remove duplicate characters from a string.
'''
n = input("Enter a string: ")
s = list(n)
s2 = []
for i in s:
    if i not in s2:
        s2.append(i)

n = "".join(s2)
print(f"New string is: {n}") 