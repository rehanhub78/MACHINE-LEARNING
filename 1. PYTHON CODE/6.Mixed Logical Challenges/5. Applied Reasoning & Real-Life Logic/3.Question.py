'''
Validate a password (at least one uppercase, lowercase, digit, special char).
'''
password = "MyPass123!"
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_characters = "!@#$%^&*()-+"
for char in password:
    has_upper |= char.isupper()
    has_lower |= char.islower()
    has_digit |= char.isdigit()
    has_special |= char in special_characters
if all([has_upper, has_lower, has_digit, has_special]):
    print("Valid password")
else:
    print("Invalid password")