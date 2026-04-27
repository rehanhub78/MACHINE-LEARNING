'''
Replace all occurrences of a character (say 'a' → 'x') recursively.
'''
def remove_occurance(s,i=0):
    if i >= len(s):
        return ""
    if s[i] == "a":
        return 'x' + remove_occurance(s, i + 1)
    return s[i] + remove_occurance(s, i + 1)
    print()

ch = str(input("Enter your string: "))
print(f"String after witout space is: {remove_occurance(ch.lower())} ")
