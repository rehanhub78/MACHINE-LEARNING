'''
Print the first and last character of a string.
'''
input_string = input("Enter a string: ")
if input_string:
    first_character = input_string[0]
    last_character = input_string[-1]
    print("The first character of the string is:", first_character)
    print("The last character of the string is:", last_character)
else:
    print("The string is empty.")