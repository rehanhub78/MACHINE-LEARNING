'''
Count consonants and vowels separately using recursion.
'''
vow = ["a","e","i","o","u"]
def count_string(s,vow_count=0,const_count=0):
    if len(s) == 0:
        print(f"Total number of vowels is: {vow_count} \nTotal number of consonants is: {const_count} ")
        return
    elif s[0].lower() in vow:
        return count_string(s[1:],vow_count+1,const_count)
    elif s[0].isalpha():
        return count_string(s[1:],vow_count,const_count+1)
    else:
        return count_string(s[1:],vow_count,const_count)
ch = str(input("Enter your string: "))
count_string(ch)
