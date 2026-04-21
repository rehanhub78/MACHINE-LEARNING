'''
Print the binary representation of all EVEN numbers from 0-n.
'''
try:
    num = int(input("Enter your number: "))
except ValueError:
    print("Invalid! Please enter numeric digits.")
    exit()

n = abs(num)

for i in range(0, n + 1):
    if i == 0:
        print("0")
    elif i % 2 == 0:
        binary = ""
        temp = i
        while temp > 0:
            binary = str(temp % 2) + binary
            temp //= 2
        if num >= 0:
            print(binary)
        else:
            print(f"-({binary})")