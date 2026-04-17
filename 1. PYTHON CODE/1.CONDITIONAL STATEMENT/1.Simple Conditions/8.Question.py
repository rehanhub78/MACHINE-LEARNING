'''
Take a character and check whether it's uppercase, lowercase, a digit, or a special character. 
'''
a = input("Enter a character: ")
if a.isupper():
    print(a,"is Uppercase.")
elif a.islower():
    print(a,"is Lowercase.")
elif a.isdigit():
    print(a,"is Digit.")
else:
    print(a,"is Special Character")
