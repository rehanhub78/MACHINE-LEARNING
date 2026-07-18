'''
Count how many prime numbers are there in an array.
'''
def count_prime(arr):
    count = 0
    for num in arr:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                count += 1
    return count
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Number of prime numbers in the array: {count_prime(arr)}")