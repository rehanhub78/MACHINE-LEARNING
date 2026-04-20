'''
 Print all numbers that are palindromes between 1-500. 
'''
for i in range(1,501):
        temp = i
        reverse = 0
        while temp > 0:
            last_digit = temp % 10
            reverse = (reverse*10) + last_digit
            temp = temp //10
        
        if i == reverse:
            print(i)
            
    
