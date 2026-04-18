'''
Print the reverse of a given number. 
'''
try:
    n = int(input("Enter your number: "))
    digits = [int(d) for d in str(abs(n))]
    if n<0:
        print("-",end="")
        
    for i in range(len(digits)):
        print(digits[-1-i], end="") 

except ValueError:
    print("Invalid! enter numeric digit.")

