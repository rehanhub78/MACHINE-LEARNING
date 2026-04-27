'''
Print all characters of a string one by one recursively.
'''
def char_string(s,i=0):
    if i < len(s):
        print(s[i])
        char_string(s,i+1)

ch = str(input("Enter your string: "))
print(f"The Characters of the String are:")
char_string(ch.lower())
