'''
 Take a password string and check basic rules (length ≥ 8 and contains at least one digit).
'''

while True:
    password = input("Enter your password: ")
    if len(password)<8 :
        print("Enter a password with more than 8 digits.")
        continue

    if any(char.isdigit() for char in password):
        print("Your Password is correct.")
        break
    else:
        print("Invalid! password must contain one digit.")
        continue
