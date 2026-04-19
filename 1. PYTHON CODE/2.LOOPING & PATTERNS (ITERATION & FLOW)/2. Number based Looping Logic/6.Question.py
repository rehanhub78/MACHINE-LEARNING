'''
print all prime number between 1 to 100.
'''
for i in range(2,101):
    is_prime = True
for j in range(2,i):
    if i % j == 0:
        is_prime = False
        break
if is_prime:
    print(i)
    
    