'''
Check if an amount can be evenly divided into 2000, 500, and 100 currency notes. 
'''
a = int(input("Enter the amount: "))
if a%2000==0 or a%500==0 or a%100==0:
    print("Yes ,amount can be evenly divided into 2000, 500, and 100 currency notes.")
else:
    print("No ,amount can not be evenly divided into 2000, 500, and 100 currency notes.")