class Student:
    college_name = "ABC college"
    def __init__(self,name):
        self.__name = name

    def hell(self):
        print(f"Hello {self.__name}")

    @staticmethod
    def hello():
        print("Hello world")


s1 = Student("Raghu")
print(s1.hell())