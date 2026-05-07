'''
Convert all characters of a string to lowercase.
'''
input_string = input("Enter a string: ")
if input_string:
    manual_lower = ""
    for char in input_string:
        if 'A' <= char <= 'Z':
            manual_lower += chr(ord(char) + 32)
        else:
            manual_lower += char
    print("The string in lowercase is:", manual_lower)
else:
    print("The string is empty.")