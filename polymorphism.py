class vehicle:
  def __init__(self, brand, model):
        self.brand = brand
        self.model = model

  def move(self):
      print("move....")

class bike(vehicle):
   pass

  #def move(self):
      #print("raceing?????")

class car(vehicle):

  def move(self):
      print("drive?????")

class cycle(vehicle):

  def move(self):
      print("paidal???")

obj1 = bike("hero", "super splendor")
obj2 = car("hyundi", "creata")
obj3 =cycle("monster", "atlas")

for x in (obj1, obj2, obj3):
  print(x.brand)
  print(x.model)
  x.move()