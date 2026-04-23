'''
Reverse a number recursively.
'''
def get_reverse(n):
    if n == 0:
        return 0
    else:
        print(n % 10, end="")
        return get_reverse(n // 10)

try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()

print(f"The reverse of the number {num} is: ", end="")
if num < 0:
    print("-", end="")
get_reverse(abs(num))
print()
print()