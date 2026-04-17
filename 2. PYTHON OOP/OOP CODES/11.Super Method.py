# super() method is used to access methods of the parent class.
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stoped.")

class Toyota(Car):
    def __init__(self, name , type):
        self.name = name
        super().start()
        super().__init__(type)


car1 = Toyota("prius", "electric")
print(car1.type)