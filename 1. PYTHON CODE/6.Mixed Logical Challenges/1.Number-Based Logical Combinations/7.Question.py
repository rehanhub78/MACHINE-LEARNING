'''
Print all prime numbers between 1 and N.
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
try:
    N = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()
    
print(f"Prime numbers between 1 and {N}:")
for num in range(2, N + 1):
    if is_prime(num):
        print(num, end=" ")