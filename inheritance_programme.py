class animal:

  def__init__(self, vegetarian, non_vegetarian):
    Self.vegetarian = input("enter the vegetarian animal name")
    Self.non_vegetarian = input("enter the non vegetarian animal name")

  def eat(self):
    print("every animal eat food")

  def slepp(self):
    print("every animal must sleep")

  def run(self):
    print("every animal can run but not all animal can run fast")

  def eating(self, pet = none):
    if pet:
       print("pet is vegetarian")
    else:
       print("pet is non vegetarian")

class cat_species(animal):

  def__init__(self, vegetarian, non_vegetarian, both):
    super().__init__(vegetarian, non_vegetarian)
    Self.both = both

  def eating_behaviour(self):
      print(" cat species basically are nonvegetarian")


class lion(cat_species):
    def display(self):
        print(" lion belong to", self.name, "species family")

class tiger(cat_species):
    def run(self):
        print("tiger can run fast as compared to the other animal like lion also")

class panther(cat_species):
    def run(self):
        print(" in cat species panther is fastest animal")

class dog(animal):

  def__init__(self, vegetarian, non_vegetarian, breed):
    super().__init__(vegetarian, non_vegetarian)
    self.breed = breed

  def eating_behaviour(self):
    print("dog species are vegitarian and non vegitarian also")

class lebra(dog):
  def behaviour(self):
    print("lebra is human friendly animal")

class bulldog(dog):
  def behaviour(self):
    print("bulldog is dangerious dog in dog species")