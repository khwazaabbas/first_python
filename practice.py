import math

class calculator:
    def __init__(self):
        self.x = int(input("enter the x value :  "))
        self.y = int(input("enter the y value :  "))
        self.add()
    
    def add(self):
        after_adding = self.x + self.y
        print("The addition of", self.x, "and", self.y, "is : ", after_adding)

class calculation(calculator):
    def __init__(self):
        super().__init__()
        self.sub()

    def sub(self):
        result = self.x - self.y
        print("The substraction of", self.x, "and", self.y, "is : ", result)

class evaluation(calculation):
    def __init__(self):
        super().__init__()
        self.div()

    def div(self):
        if self.y != 0:
            result = self.x / self.y
            print("The division of", self.x, "and", self.y, "is : ", result)
        else:
            print("Division by zero is not allowed.")

class processing(evaluation):
    def __init__(self):
        super().__init__()
        self.mul()

    def mul(self):
        result = self.x * self.y
        print("The multiplication of", self.x, "and", self.y, "is : ", result)

calc = processing()