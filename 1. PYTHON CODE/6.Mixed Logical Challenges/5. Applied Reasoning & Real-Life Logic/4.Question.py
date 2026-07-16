'''
Simulate a simple calculator using switch-case.
'''
switcher = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = switcher.get(operation, lambda x, y: "Invalid operation")(num1, num2)
print(f"Result: {result}")