class Student:
    def __init__(self,name):
        self.name = name


a1 = Student("yash")
print(a1.name) # yash

del a1
print(a1.name) # error