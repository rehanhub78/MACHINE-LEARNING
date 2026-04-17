'''
 Check whether a number is a perfect square (without using the square root function).
'''
a = int(input("Enter the number: "))
found = False
for i in range(1,a):
    if i*i == a:
        print(a,"is a perfect square of:",i)
        found=True
        break
    elif i*i>a:
        break
if not found:
    print(a,"is not a perfect square.")

        