'''
Count how many alphabets are before 'm' and after 'm' in a given string. 
'''
def count_alphabets(string):
    before_m = 0
    after_m = 0
    found_m = False
    for char in string:
        if char == 'm':
            found_m = True
        elif char.isalpha():
            if not found_m:
                before_m += 1
            else:
                after_m += 1
    return before_m, after_m
while True:
    string = input("Enter a string: ")
    if 'm' in string:
        break
    else:
        print("The string must contain the character 'm'. Please try again.")
before_m, after_m = count_alphabets(string) 
print(f"Number of alphabets before 'm': {before_m}")
print(f"Number of alphabets after 'm': {after_m}")