'''
Remove all spaces from a string recursively.
'''
space = " "
def remove_space(s, i=0):
    if i >= len(s):
        return ""
    if s[i] == " ":
        return remove_space(s, i + 1)
    return s[i] + remove_space(s, i + 1)
    print()

ch = str(input("Enter your string: "))
print(f"String after witout space is: {remove_space(ch)} ")
