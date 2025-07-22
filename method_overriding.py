class humans:
    def eating(self):
        print("humans are vegetarian and non vegetarian ")
    def operation(self, a = None, b = None, c = None, d = None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        if a!=None and b!=None and c!=None and d!=None:
            print(self.a / self.b / self.c /self.d)
        elif a!=None and b!=None and c!=None:
            print(self.a * self.b * self.c)
        elif a!=None and b!=None:
            print(self.a + self.b)
        else:
            print("enter atleast two values")
           
values = input("Enter values separated by spaces: ").split()

values = [float(v) for v in values]

mani = humans()
if len(values)>4:
    print("enter upto 4 digit")
else:

    mani.operation(*values[:4])

class male(humans):
    def short_hair(self):
        print("males usually have short hair")
        

class female(humans):
    def long_hair(self):
        print("female usually have long hair")

class boy(male):
    def black(self):
        print("boys like black color")

class girl(female):
    def pink(self):
        print("girls like pink color")