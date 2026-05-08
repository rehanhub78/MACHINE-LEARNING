'''
Print the ASCII value of each character in a string.
'''
str1 = input("Enter a string: ")
for char in str1:
    print(f"The ASCII value of {char} is: {ord(char)}")

