class eatables:
    hunger = True
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def common(self):
        print("eatable things are common in all over the world")

class vegetables(eatables):
    def taste(self):
        print("rich taste with iron")
        super().common()

class fruits(eatables):
    def taste(self):
        print("sweet taste with kind of minerals")
        super().common()

class milk_products(eatables):
    def taste(self):
        print("milk is a complete diet with lots of minerals and vitamins")
        super().common()

class chocolate(eatables):
    def taste(self):
        print("Dark chocolate has a stronger taste compared to normal chocolate")
        super().common()

obj1 = eatables("tofee", "brown")
obj2 = vegetables("potato", "light_brown")
obj3 = fruits("mango", "yellow")
obj4 = milk_products("rabdi", "white")
obj5 = chocolate("dark_choco","black&white")

print(obj1.name, obj1.color)
print(obj2.name, obj2.color)
print(obj3.name, obj3.color)
print(obj4.name, obj4.color)
print(obj5.name, obj5.color)
obj1.common()
obj2.taste()
obj3.taste()
obj4.taste()
obj5.taste()
print(obj1.hunger)