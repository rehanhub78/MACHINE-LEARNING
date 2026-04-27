'''
Remove all occurrences of a character from a string recursively. 
'''
def remove_occurence(s,x,i=0):
    if i >= len(s):
        return ""
    if s[i] == x:
        return remove_occurence(s,x,i+1)
    return s[i] + remove_occurence(s,x,i+1)

ch = str(input("Enter your string: "))
b = str(input("Enter character to remove: "))
if len(b) == 1:
    print(f"String after removing {b} is: {remove_occurence(ch.lower(),b.lower())} ")
else:
    print(f"Invalid! Please enter a valid character.")