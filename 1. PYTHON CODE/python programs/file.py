''' f = open("demo.txt","a+")
data = f.read()
print(data)
f.write("this is overwriting ")
f.close() '''
# OPPENING A FILE USING "WITH"
'''with open("demo.txt","r") as f:
   data = f.read()
   print(data)'''
# DELETING A FILE 
# using the os module 
'''import os
os.remove("demo.txt")'''
