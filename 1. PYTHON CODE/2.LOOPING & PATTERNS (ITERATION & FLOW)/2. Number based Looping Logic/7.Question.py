'''
check user number is a prime number.
'''
try:
    n = int(input("Enter your number: "))
    num = n
    div = 1
    if n<0:
        print("Invalid! Please enter a positive number.")
    elif n in range(0,2):
        print(f"Your number {n} is not a prime number")
    else:
        is_prime = True
        for i in range(2,n):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"your number {n} is a prime number.")
        else:
            print(f"Your number {n} is a not prime number")
                
except ValueError:
    print("Invalid! Please enter numeric digits.")

