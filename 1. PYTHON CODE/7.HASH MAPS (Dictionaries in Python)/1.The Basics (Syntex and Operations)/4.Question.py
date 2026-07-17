'''
Merge two different dictionaries into a single dictionary.if a key exist in both ,keep the value from the second dictionary.
'''
student1 = {"rehan":82 , "rohit":55 ,"alex":78}
student2 = {"beemn":87 , "mohit":75 ,"alex":98}

merge_student = student1 | student2
for key,value in merge_student.items():
    print(f"Key: [{key}], Value: [{value}]")
