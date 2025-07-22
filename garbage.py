class mathematics:
    def greet(self):
        print("basically mathematics used for diff kind for calculation and problem solving")
        
class addition(mathematics):
    def add(self):
        self.a = int(input(" enter the first number : "))
        self.b = int(input("enter the second number : "))
        result = self.a + self.b
        print("the sum of",self.a, "and", self.b, "=", result)
        
        
        
class substraction(mathematics):
    def sub(self, x, y):
        self.x = x
        self.y = y
        result = self.x - self.y
        print("the substraction of", self.x, "and", self.y, "=", result)
        
        
class multiplication(mathematics):
    def mul(self):
        self.m = int(input("enter the first no. for mul : "))
        self.n = int(input("enter the second no. for mul : "))
        result = self.m * self.n
        print("the multplication of", self.m, "and", self.n, "=", result)
        
class division(mathematics):
    def div(self):
        self.p = int(input(" enter the 1st number for div : "))
        self.q = int(input(" enter the 2nd number for div : "))
        result = self.p / self.q
        print("the division of", self.p, "and", self.q, "=", result)
        
obj = addition()
obj.greet()
obj.add()
obj2 = substraction()
obj2.greet()
obj2.sub(44, 32)
obj3 = multiplication()
obj3.mul()
obj4 = division()
obj4.greet()
obj4.div()