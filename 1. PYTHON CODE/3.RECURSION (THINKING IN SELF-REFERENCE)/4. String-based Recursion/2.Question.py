'''
Check if a string is palindrome using recursion.
'''
def string(s):
    if len(s) <=1:
        return s
    else:
        return string(s[1:]) + s[0]
    
ch = str(input("Enter your string: "))
b = string(ch)
if ch == b:
    print(f"String is palindrome.")
else:
    print(f"String is not palindrome.")
    