# Wrapping data and function into a single unit(object)
class Account:
    def __init__(self, bal, accno):
        self.balance = bal
        self.account_no = accno
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited \n Your remainig balance is: ",self.balance)
    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited \n Your new balance is: ",self.balance)
        
        
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
