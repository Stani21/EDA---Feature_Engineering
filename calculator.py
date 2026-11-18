
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        add = self.a + self.b
        return add

    def multiply(self):
        sub = self.a - self.b
        return sub
    
    def show_numbers(self):
        return self.a, self.b
