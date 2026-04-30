'''
Find the count of prime numbers in the array. 
'''
n = int(input("Enter how many numbers you want to store in the array: "))
if n <= 0:
    print("Invalid! Please enter a positive integer.")
    exit()
    
my_array = []
while len(my_array) < n:
    try:
        num = int(input(f"Enter number {len(my_array) + 1}: "))
        my_array.append(num)
    except ValueError:
        print("Invalid! Please enter numeric digit.")
        
prime_count = 0
for i in my_array:
    if i > 1:
        is_prime = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
print(f"Count of prime numbers in the array: {prime_count}")


