'''
Print the sum of all odd digits and even digits separately in a number.
'''
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
n = abs(num)
digits = [int(d) for d in str(n)]
even_sum = 0
odd_sum = 0

for i in digits:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Sum of even digits: {even_sum}")
print(f"Sum of odd digits: {odd_sum}")
    
