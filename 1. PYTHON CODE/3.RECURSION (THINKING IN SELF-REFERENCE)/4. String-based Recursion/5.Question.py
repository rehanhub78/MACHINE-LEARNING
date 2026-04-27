'''
Replace all occurrences of a character (say 'a' → 'x') recursively.
'''
def replace_occurance(s,i=0):
    if i >= len(s):
        return ""
    if s[i] == "a":
        return 'x' + replace_occurance(s, i + 1)
    return s[i] + replace_occurance(s, i + 1)

ch = str(input("Enter your string: "))
print(f"String after witout space is: {replace_occurance(ch.lower())} ")
