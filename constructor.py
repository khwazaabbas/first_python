class abbas:
    def __init__(self):
        self.x = int(input("enter the X value :  "))
        self.y = int(input("enter the Y value :  "))
        self.show()
        self.addition()
        self.multiplication()
        self.division()
        self.substraction()

    def show(self):
        print("X value is : ", self.x)
        print("Y value is : ", self.y)

    def addition(self):
        result = self.x + self.y
        print("The addition of", self.x, "and", self.y, "is : ", result)

    def multiplication(self):
        result = self.x * self.y
        print("The multiplication of", self.x, "and", self.y, "is : ", result)

    def division(self):
        result = self.x / self.y
        print("The division of", self.x, "and", self.y, "is : ", result)

    def substraction(self):
        result = self.x - self.y
        print("The substraction of", self.x, "and", self.y, "is : ", result)

    

class mani(abbas):
    def __init__(self):
        super().__init__()
        self.z = int(input("enter the Z value :  "))
        self.show_z()
        self.addition_z()
        self.multiplication_z()
        self.division_z()
        self.substraction_z()

    def show_z(self):
        print("Z value is : ", self.z)

    def addition_z(self):
        result = self.x + self.y + self.z
        print("The addition of", self.x, ",", self.y, "and", self.z, "is : ", result)

    def multiplication_z(self):
        result = self.x * self.y * self.z
        print("The multiplication of", self.x, ",", self.y, "and", self.z, "is : ", result)

    def division_z(self):
        result = self.x / self.y / self.z
        print("The division of", self.x, ",", self.y, "and", self.z, "is : ", result)

    def substraction_z(self):
        result = self.x - self.y - self.z
        print("The substraction of", self.x, ",", self.y, "and", self.z, "is : ", result)



class sani(mani):
    def __init__(self):
        super().__init__()
        self.w = int(input("enter the W value :  "))
        self.show_w()
        self.addition_w()
        self.multiplication_w()
        self.division_w()
        self.substraction_w()

    def show_w(self):
        print("W value is : ", self.w)

    def addition_w(self):
        result = self.x + self.y + self.z + self.w
        print("The addition of", self.x, ",", self.y, ",", self.z, "and", self.w, "is : ", result)

    def multiplication_w(self):
        result = self.x * self.y * self.z * self.w
        print("The multiplication of", self.x, ",", self.y, ",", self.z, "and", self.w, "is : ", result)

    def division_w(self):
        result = self.x / self.y / self.z / self.w
        print("The division of", self.x, ",", self.y, ",", self.z, "and", self.w, "is : ", result)

    def substraction_w(self):
        result = self.x - self.y - self.z - self.w
        print("The substraction of", self.x, ",", self.y, ",", self.z, "and", self.w, "is : ", result)
    
    



a = abbas()
b = mani()
c = sani()