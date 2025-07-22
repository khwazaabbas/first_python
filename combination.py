import this
import math

class mathematics:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class addition(mathematics):

    def add(self):
        return self.a + self.b
    
class subtraction(mathematics):

    def subtract(self):
        return self.a - self.b
    
class multiplication(mathematics):

    def multiply(self):
        return self.a * self.b
    
class division(mathematics):

    def divide(self):
        if self.b ==0:
            return "division by zero in not allowed according to rules of mathematics"
        else:
            return self.a / self.b
        


class area_of_triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangle_area(self):
        s = (self.a + self.b + self.c) /2
        area = math.sqrt( s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

class area_of_cube:
    def __init__(self, a):
        self.a = a
    def cube_area(self):
        area = 6 * self.a * self.a
        return area
    
class area_of_circle:
    def __init__(self, r):
        self.r = r

    def circle_area(self):
        return math.pi * self.r * self.r
    
class calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error: Division by zero is not allowed."
        return x / y

print("Select operation:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: Exit")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print("Result:", calculator.add(num1, num2))
        elif choice == '2':
            print("Result:", calculator.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calculator.multiply(num1, num2))
        elif choice == '4':
            print("Result:", calculator.divide(num1, num2))
    else:
        print("Invalid choice. Please select a valid option.")