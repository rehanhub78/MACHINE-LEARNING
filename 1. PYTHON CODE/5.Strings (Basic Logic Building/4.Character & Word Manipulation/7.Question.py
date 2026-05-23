'''
Keep only the first occurrence of each character.
'''
n = input("Enter a string: ")
s = list(n)
s2 = []
for i in s:
    if i not in s2:
        s2.append(i)
print(f"String with only first occurrences: {"".join(s2)}")