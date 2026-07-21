'''
Take two arrays(one of keys,one of values) and map them together into a single dictionary.
'''
keys = ["a" , "b" , "c" , "d"]
values = [9 , 10 , 56 , 78]

my_dic = dict(zip(keys , values))
print(my_dic)