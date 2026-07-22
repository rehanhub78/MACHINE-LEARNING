'''
Create a dictionary where the keys are numbers from 1 to n, and the values are the squares of those numbers.
'''
n = 10
arr =[x for x in range(1,n+1)]
sq_arr = [x**2 for x in arr]
sqr_dict = dict(zip(arr , sq_arr))

print(sqr_dict)

squared_dict = {x:x**2 for x in range(1,n+1)} #Direct method