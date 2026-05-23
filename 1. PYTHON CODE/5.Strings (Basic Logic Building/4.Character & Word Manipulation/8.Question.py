'''
Remove consecutive duplicate characters (e.g., “aaabb” → “ab”).
'''
n = input("Enter a string: ")
s = list(n)
s2 = []
for i in range(len(s)):
    if i == 0 or s[i] != s[i-1]:
        s2.append(s[i])
print(f"String with consecutive duplicates removed: {"".join(s2)}")