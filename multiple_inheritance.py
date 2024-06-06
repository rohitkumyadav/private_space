class A:
    v1 = "Welcome to class A"

    @staticmethod
    def start():
        print("Start")

class B(A):
    v2 = "Welcome to class B"
    def __init__(self, name,type):
        # super().__init__(name)  # This line is not needed since class A does not have an __init__ method
        self.name = name
        self.type = type
s1 = B("namssse","frusto")
print(s1.name)
print(s1.type)
