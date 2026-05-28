'''
Check if two strings are anagrams (without using collections).
'''
a = input("Enter the first string: ")
b = input("Enter the second string: ")
a = a.replace(" ", "").lower()
b = b.replace(" ", "").lower()

if sorted(a) == sorted(b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")