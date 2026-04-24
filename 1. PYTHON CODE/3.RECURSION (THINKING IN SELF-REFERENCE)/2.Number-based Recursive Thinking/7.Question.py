'''
Print digits of a number in words recursively (e.g., 123 → “one two three”).
'''
NAMES = ["zero","One","Two","Theree","Four","Five","Six","Seven","Eight","Nine"]
def digits_name(n):
    if n < 10:
        return NAMES[n]
    else:
        return digits_name(n // 10) + " " + NAMES[n % 10]
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digit.")
    exit()
if num < 0:
    print(f"Digits of {num} in words is: -{digits_name(abs(num))}")
else:
    print(f"Digits of {num} in words is: {digits_name(num)}")