'''
Compare two strings lexicographically (like dictionary order).
'''
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str1.lower() < str2.lower():
    print(f"First string '{str1}' is lexicographically comes first.")
elif str1.lower() > str2.lower():
    print(f"Second string '{str2}' is lexicographically comes first.")
else:
    print(f"Both strings '{str1}' and '{str2}' are equal.")