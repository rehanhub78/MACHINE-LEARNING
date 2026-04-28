'''
Convert a string to uppercase recursively.
'''
def upper_case(s,i=0):
    if i < len(s):
        print(s[i].upper(), end="")
        upper_case(s,i+1)

ch = str(input("Enter your string: "))
print(f"The String in uppercase is:")
upper_case(ch)
