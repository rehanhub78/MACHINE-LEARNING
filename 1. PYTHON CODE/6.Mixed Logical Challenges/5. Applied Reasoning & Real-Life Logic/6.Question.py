'''
Print frequency of each digit in a number.
'''
num = input("Enter a number: ")
frequency = {}
for digit in num:
    frequency[digit] = frequency.get(digit, 0) + 1
for digit, count in frequency.items():
    print(f"Digit {digit}: {count} times")
