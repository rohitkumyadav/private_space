class Car:
    @staticmethod
    def start():
        print("Car started")

class Toyata(Car):
    def __init__(self, name):
        self.name =  name


car1 = Toyata("RAV4")
print(car1.name)
car1.start()