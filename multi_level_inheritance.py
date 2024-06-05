class Car:
    @staticmethod
    def start():
        print("Car started")

class Toyata(Car):
    def __init__(self, brand):
        self.name =  brand

class Company(Toyata):
    def __init__(self,type):
        self.type = type


t1  = Company("diesel")
t1.start() 