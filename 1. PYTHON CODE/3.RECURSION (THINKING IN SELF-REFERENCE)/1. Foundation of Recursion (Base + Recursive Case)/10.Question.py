'''
 Find sum of digits of a number recursively. 
'''
def get_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + get_sum(n // 10)

try:
    num = int(input("enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
final_sum = get_sum(abs(num))
print(f"The sum of the digits is: {final_sum}")
