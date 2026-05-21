'''
Remove all spaces from a string.
'''
n = input("Enter a string: ")
s = [x for x in n if x != " "]
print(f"string without vowels is: {"".join(s)}")
