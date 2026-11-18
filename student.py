class Student:
    def __init__(self):
        self.name = "Stanish"
        self.age = 24

    def greet(self):
        print(f"Hello,My name is {self.name}")

    def get_age(self):
        return self.age