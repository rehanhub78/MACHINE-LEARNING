class Car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stoped.")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("disel")
car1.start()

