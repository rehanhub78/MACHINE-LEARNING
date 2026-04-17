'''
Take a single digit (0-9) and print its word form (“Zero” to “Nine”). 
'''
try:
    a = int(input("Enter a single digit (0-9): "))
    b = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    if a in range(0,10):
        print(b[a])
    else:
        print("Your number is not single digit.")
except ValueError:
    print("Invalid input! Please enter a numeric digit.")