'''
Sort a dictionary by its values instead of its keys (returning a list of tuples or a newly sorted dictionary).
'''
my_dict = {"a":18 , "b":23 , "c":13 , "d":22 , "e":43}

sorted_list = sorted(my_dict.items(), key=lambda item: item[1])
print(sorted_list)