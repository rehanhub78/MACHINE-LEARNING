# this means to be used only within the class and are not accessible from outside the class.
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # "__" convert acc_pass to private attribute

    def privateaccess(self): # this method access a private attribute
        print(self.__acc_pass)
      

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.privateaccess())                                  
