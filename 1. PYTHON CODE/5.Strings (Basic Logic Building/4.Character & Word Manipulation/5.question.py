'''
Print the string after removing all digits.
'''
n = input("Enter a string: ")
digit = "1234567890"
s = [x for x in n if x not in digit]
print(f"New string is: {"".join(s)}")
