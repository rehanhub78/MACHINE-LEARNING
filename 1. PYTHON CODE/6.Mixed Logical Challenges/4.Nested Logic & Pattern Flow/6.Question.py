'''
Find all pairs of characters in a string that are the same (nested loop).
'''
s = "aaaaabbcc"
pairs = []
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            pairs.append((s[i], i, j))
print(f"Pairs of same characters: {pairs}")
