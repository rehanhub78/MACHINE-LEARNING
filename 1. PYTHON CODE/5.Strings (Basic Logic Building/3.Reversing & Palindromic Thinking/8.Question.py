'''
Remove the first and last character and print the remaining string.
'''
n = input("Enter a string: ")
s = list(n)
s.pop(0)
s.pop(-1)
print(f"Updated string is: {"".join(s)}")