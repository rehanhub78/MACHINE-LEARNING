'''
Swap case: uppercase → lowercase and lowercase → uppercase.
'''
n = input("Enter a string: ")
s = list(n)
s2 = []
for i in s:
    if i.isupper():
        s2.append(i.lower())
    else:
        s2.append(i.upper())
print(f"String with swapped case: {"".join(s2)}")