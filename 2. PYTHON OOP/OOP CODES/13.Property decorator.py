# we use @property decorator on any method in the class to use the method as a property.
class Student :
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
    @property
    def percentage(self):
        return str((self.phy +self.che + self.math)/3) + "%"

st1 = Student(97,44,77)
print(st1.percentage)


# st1.phy = 86
# print(st1.phy)
# st1.percentage()