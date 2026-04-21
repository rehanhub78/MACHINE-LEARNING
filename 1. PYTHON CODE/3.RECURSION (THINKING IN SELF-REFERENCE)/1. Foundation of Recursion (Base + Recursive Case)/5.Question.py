'''
Print sum of first n natural numbers recursively.
'''
def get_total(a):
    if a == 0:
        return 0
    else:
        return a + get_total(a - 1)
        
try:
    n = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()
final_sum = get_total(n)
print(f"Sum of first {n} natural numbers is: {final_sum}")