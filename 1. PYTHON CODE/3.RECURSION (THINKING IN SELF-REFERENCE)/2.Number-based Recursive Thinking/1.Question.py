'''
Count the number of digits in a number recursively.
'''
def digits_count(n):
    if n in range(0,10):
        return 1
    else:
        return 1 + digits_count(n // 10)
    
try:
    num = int(input("enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
final_count = digits_count(abs(num))
print(f"The total number of digits  in {num} is: {final_count}")
