'''
Take age inputs and count how many are adults, minors, seniors. 
'''
ages = [15, 22, 34, 67, 12, 45, 78, 19, 30, 55]
adults = 0
minors = 0
seniors = 0
for age in ages:
    if age < 18:
        minors += 1
    elif 18 <= age < 60:
        adults += 1
    else:
        seniors += 1
print(f"Number of minors: {minors}")
print(f"Number of adults: {adults}")
print(f"Number of seniors: {seniors}")