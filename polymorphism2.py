class Calculator:
    def operate(self, a=None, b=None, c=None, d=None):
      self.a = a
      self.b = b
      self.c = c
      self.d = d
      
      if a!= None and b!= None and c!=None and d!=None :
            print(self.a / self.b /  self.c /self.d)
        
      elif a!= None and b!= None and c!=None :
            print(self.a*self.b*self.c)
        
      elif a!=None and b!=None :
            print(self.a + self.b)
      
      else:
            print("enter atleast two values")

# Taking user input
values = input("Enter values separated by spaces: ").split()

# Convert inputs to numbers
values = [float(v) for v in values]  # Convert to float for division handling

# Create an instance of Calculator
calc = Calculator()

# Call the method with unpacked arguments (up to 4 values)
if len(values)>4:
     print("enter upto 4 digits")
else:     
    calc.operate(*values[:4])