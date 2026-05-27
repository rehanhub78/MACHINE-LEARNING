'''
Count how many even digits a number contains.
'''
def count_even_digits(n):
    count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            count += 1
    return count
number = int(input("Enter a number: "))
print(f"The number {number} contains {count_even_digits(number)} even digits.")