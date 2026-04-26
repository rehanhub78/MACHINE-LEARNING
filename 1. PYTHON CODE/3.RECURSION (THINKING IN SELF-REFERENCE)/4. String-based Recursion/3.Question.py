'''
Count vowels in a string recursively.
'''
vow = ["a","e","i","o","u"]
def vowel_count(s, count = 0):
    if len(s) == 0:
        return count
    if s[0].lower() in vow:
        count += 1
    return vowel_count(s[1:], count)

ch = str(input("Enter your string: "))
print(f"Total number of vowels in {ch} is: {vowel_count(ch)}")
