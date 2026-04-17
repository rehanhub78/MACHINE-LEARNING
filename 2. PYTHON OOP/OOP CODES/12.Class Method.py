# A Class Method is bound to the class & receives the class as an implicit first argument.
# Note -: static method can't accesss or modify class state & generally for utility.
class Person:
    name = "anonymous"

    '''def changeName(self, name):
        # self.name = name
        # Person.name = name '1st way to change class attribute
        # self.__class__.name = "Md Rehan"  '2nd way to change class attribute
        '''
    @classmethod     #decorator
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Md Rehan")
print(p1.name)
print(Person.name)

