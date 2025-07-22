class bike:
    cycle = True

    def speed(self):
        print("speed is 100 kmph")

    def tank(self):
        print("tank capacity is 15 liter")

    def breaking(self):
        print("abs breakingb system")

class honda(bike):
    def india(self):
        print("cbr 100 cc")

class hero(bike):
    def nepal(self):
        print("super splendor 125 cc asfs")

class yamaha(bike):
    def pakistan(self):
        print("yamaha r1 1000 cc")

obj1 = honda()
obj2 = hero()
obj3 = yamaha()
obj1.breaking()
obj2.speed()
obj3.tank()

obj1.india()
obj2.nepal()
obj3.pakistan()

objbike = bike()
objbike.speed()
objbike.tank()
objbike.breaking()

print(objbike.cycle)