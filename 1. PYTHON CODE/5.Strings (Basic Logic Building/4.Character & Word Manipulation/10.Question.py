'''
Shift each character by 1 (e.g., “abc” → “bcd”).
'''
n = input("Enter a string: ")
s = list(n)
i = 0
while i < len(s):
    if s[i].isalpha():
        s[i] = chr(ord(s[i]) + 1)
    elif s[i].isdigit():
        s[i] = chr((ord(s[i]) - ord('0') + 1) % 10 + ord('0'))
    i += 1
print(f"String with characters shifted by 1: {''.join(s)}")