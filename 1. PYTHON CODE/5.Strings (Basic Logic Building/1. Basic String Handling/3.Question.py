'''
Convert all characters of a string to uppercase.
'''
input_string = input("Enter a string: ")
if input_string:
    manual_upper = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            manual_upper += chr(ord(char) - 32)
        else:
            manual_upper += char
    print("The string in uppercase is:", manual_upper)
else:
    print("The string is empty.")