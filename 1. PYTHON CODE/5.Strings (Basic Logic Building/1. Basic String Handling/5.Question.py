'''
Count how many characters (excluding spaces) are in the string.
'''
input_string = input("Enter a string: ")
if input_string:
    char_count = 0
    for char in input_string:
        if char != " ":
            char_count += 1
    print("The number of characters (excluding spaces) is:", char_count)
else:
    print("The string is empty.")
    