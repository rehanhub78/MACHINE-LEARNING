'''
Count how many substrings start and end with the same character (simple logic).
'''
from collections import Counter
def count_substrings(s):
    freq = Counter(s)
    count = 0
    for char, n in freq.items():
        count += n * (n + 1) // 2
    return count
n = input("Enter your string: ")
print(f"Number of total substrings start and end with the same character is: {count_substrings(n)}")
